import msvcrt as m
import game.functions as f
import game.game_mode_1 as gm1
import game.game_mode_2 as gm2
import game._highscore as h
import game.save_load as sl
from os import system, name

def splash_screen():
    while True:
        system("cls" if name == "nt" else "clear")
        print("""
-----------------------------
Game rules are as follows!
        
1. The word must be Swedish.
2. The word must be 5 letters.
3. The word must not be a name.
4. The word must not have tense inflection.
5. The word must not have plural conjugation.
6. The word must not have repeated letters, such as 'sit'.

Type 'yes' to accept the rules and start the game.
Type 'no' to deny the rules and end the game.""")
    
        accept = input("\nDo you accept these rules?: ").lower()
        if accept == "yes":
            system("cls" if name == "nt" else "clear")
            main_menu()
        elif accept == "no":
            print("Then you will not be allowed to join the game.\Exiting the game.")
            exit()
        else:
            print("""\nPlease accept the game rules in order to play.
Type 'yes' to accept the rules and start the game.
Type 'no' to deny the rules and end the game.
Press any key to continue.""")
            m.getch()


def main_menu():   
    
    
    while True:
        f.remove_hints() # To remove hints from previous game, if still there  
        print("""
----------MAIN MENU----------
| 1. Play as guesser        |
| 2. Play as a thinker      |
-----------------------------
| 3. Load game              |
| 4. Delete saved game      |
| 5. See current highscore  |
-----------------------------
| 8. Reset highscore        |
| 9. Exit                   |
-----------------------------
""")  
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                gm1.game_func(num_of_guesses=0, word="", guessed_words=[])
            elif choice == 2:
                gm2.game_func_2()
            elif choice == 3:
                load = sl.load_into_gm()
                if load == FileNotFoundError:
                    print("Choose another option.\nPress any key to continue.")
                    m.getch()
                else:
                    num_of_guesses = load[0]
                    word = load[1]
                    guessed_words = load[2]
                    print("\nYour game has been loaded!\n")
                    print("Press any key to continue.")
                    m.getch()
                    gm1.game_func(num_of_guesses, word, guessed_words)
            elif choice == 4:
                sl.delete_save()
            elif choice == 5:
                try:
                    h.print_highscore()
                except ValueError:
                    print("There are no highscores yet.")
                print("\nPress any key to continue.")
                m.getch()
            elif choice == 8:
                h.reset_highscore()
            elif choice == 9:
                f.quit_game()
        except ValueError:
            print("You must enter the number that matches the choice you want to make.")
            print("Press any key to continue.")
            m.getch()
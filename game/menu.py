import msvcrt as m
import game.functions as f
import game.game_mode_1 as gm1
import game.game_mode_2 as gm2
import game._highscore as h
import game.save_load as sl

def splash_screen():
    
    print("""
-----------------------------
Spelregler är som följer!
        
1. Ordet måste vara svenskt.
2. Ordet måste vara 5 bokstäver.
3. Ordet får inte vara ett namn.
4. Ordet får inte ha tempus-böjning.
5. Ordet får inte ha plural-böjning.
6. Ordet får inte ha upprepade bokstäver, så som 'sitta'.

Skriv 'ja' för att acceptera reglerna och börja spelet.
Skriv 'nej' för att neka reglerna och avsluta spelet.""")
    
    accept = input("\nAccepterar du spelreglerna? ").lower()
    if accept == "ja":
        main_menu()
    elif accept == "nej":
        print("Då får du inte lov att vara med och spela.\nAvslutar spelet.")
        exit()
    else:
        print("\nVänligen acceptera spelreglerna för att kunna spela.\n\nSkriv 'ja' för att acceptera reglerna och börja spelet.\nSkriv 'nej' för att neka reglerna och avsluta spelet.\n\nTryck på valfri tangent för att fortsätta.")
        m.getch()
        splash_screen()


def main_menu():   
    
    
    while True:
        f.remove_hints() # To remove hints from previous game, if still there  
        
        print("""
----------MAIN MENU----------
| 1. Spela som gissare      |
| 2. Spela som tänkare      |
-----------------------------
| 3. Ladda spel             |
| 4. Radera sparat spel     |
| 5. Se nuvarande highscore |
-----------------------------
| 8. Återställ highscore    |
| 9. Avsluta                |
-----------------------------
""")  
        try:
            choice = int(input("Välj ett alternativ: "))
            if choice == 1:
                gm1.game_func_1(num_of_guesses=0, word="", guessed_words=[])
            elif choice == 2:
                gm2.game_func_2()
            elif choice == 3:
                load = sl.load_into_gm()
                if load == FileNotFoundError:
                    print("Tryck på valfri tangent för att fortsätta.")
                    m.getch()
                else:
                    num_of_guesses = load[0]
                    word = load[1]
                    guessed_words = load[2]
                    print("\nDitt spel har laddats!\n")
                    gm1.game_func_1(num_of_guesses, word, guessed_words)
            elif choice == 4:
                sl.delete_save()
            elif choice == 5:
                try:
                    h.print_highscore()
                except ValueError:
                    print("Det finns inga highscores än.")
                print("\nTryck på valfri tangent för att fortsätta.")
                m.getch()
            elif choice == 8:
                h.reset_highscore()
            elif choice == 9:
                f.quit_game()
            else:
                print("Du måste ange siffran som stämmer överens med det val du vill göra.")
        except ValueError:
            # print("Vänligen ange ett giltligt alternativ.")
            pass




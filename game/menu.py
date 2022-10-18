import game.functions as f
import game.game_mode_1 as gm1
import game.game_mode_2 as gm2
import game._highscore as h
import game.save_load as sl
import game.word_functions as w
from os import system, name

clr_screen = system("cls" if name == "nt" else "clear")


def splash_screen():
    while True:
        f.clear_screen()
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

        accept = input("\nAccepterar du spelreglerna?: ").lower()
        if accept == "ja":
            f.clear_screen()
            main_menu()
        elif accept == "nej":
            print(
                "Då får du inte lov att vara med och spela.\nAvslutar spelet.")
            exit()
        else:
            print("""\nVänligen acceptera spelreglerna för att kunna spela.
Skriv 'ja' för att acceptera reglerna och börja spelet.
Skriv 'nej' för att neka reglerna och avsluta spelet.""")
            input("Tryck på valfri tangent för att fortsätta...")


def main_menu():

    while True:
        print("""
----------MAIN MENU----------   --------------------Spelregler är som följer!--------------------
| 1. Spela som gissare      |   |    1. Ordet måste vara svenskt.                               |
| 2. Spela som tänkare      |   |    2. Ordet måste vara 5 bokstäver.                           |
-----------------------------   |    3. Ordet får inte vara ett namn.                           |
| 3. Ladda spel             |   |    4. Ordet får inte ha tempus-böjning.                       |
| 4. Radera sparat spel     |   |    5. Ordet får inte ha plural-böjning.                       |
| 5. Se nuvarande highscore |   |    6. Ordet får inte ha upprepade bokstäver, så som 'sitta'.  |
-----------------------------   -----------------------------------------------------------------
| 8. Återställ highscore    |
| 9. Avsluta                |
-----------------------------        
""")
        try:
            choice = int(input("Välj ett alternativ: "))
            if choice == 1:
                f.clear_screen()
                gm1.game_func_1(num_of_guesses=0,
                                word=w.get_word(),
                                guessed_words=[],
                                end_of_game=False)
            elif choice == 2:
                f.remove_hints(
                )  # To remove hints from previous game, if still there
                f.clear_screen()
                gm2.game_func_2(num_of_turns=0,
                                user_word=w.player_word(),
                                python_list=w.create_word_list(),
                                end_of_game=False)
            elif choice == 3:
                choice = int(
                    input("Vill du ladda ett spel från spelläge 1 eller 2?: "))
                if choice == 1:
                    load = sl.load_game(save_file='data\save_game_1.txt')
                    if load == FileNotFoundError:
                        continue
                    else:
                        num_of_guesses = load[0]
                        word = load[1]
                        guessed_words = load[2]
                        print("\nDitt spel har laddats!\n")
                        input("Tryck på valfri tangent för att fortsätta...")
                        f.clear_screen()
                        gm1.game_func_1(num_of_guesses,
                                        word,
                                        guessed_words,
                                        end_of_game=False)
                elif choice == 2:
                    load = sl.load_game(save_file='data\save_game_2.txt')
                    if load == FileNotFoundError:
                        continue
                    else:
                        num_of_turns = load[2]
                        user_word = load[0]
                        python_list = load[1]
                        print("\nDitt spel har laddats!\n")
                        input("Tryck på valfri tangent för att fortsätta...")
                        f.clear_screen()
                        gm2.game_func_2(user_word,
                                        python_list,
                                        num_of_turns,
                                        end_of_game=False)
                else:
                    print("Du måste ange 1 eller 2.\nÅtergår till huvudmenyn.")
                    input("Tryck på valfri tangent för att fortsätta...")
            elif choice == 4:
                choice = int(
                    input(
                        "Vill du radera ett spel från spelläge 1 eller 2?: "))
                if choice == 1:
                    sl.delete_save(save_file='data\save_game_1.txt')
                elif choice == 2:
                    sl.delete_save(save_file='data\save_game_2.txt')
                else:
                    print("Du måste ange 1 eller 2.\nÅtergår till huvudmenyn.")
                    input("Tryck på valfri tangent för att fortsätta...")
                    f.clear_screen()
            elif choice == 5:
                try:
                    f.clear_screen()
                    h.print_highscore()
                    f.clear_screen()
                except ValueError:
                    print("Det finns inga highscores än.")
                    input("Tryck på valfri tangent för att fortsätta...")
                    f.clear_screen()
            elif choice == 8:
                h.reset_highscore()
                input("Tryck på valfri tangent för att fortsätta...")
                f.clear_screen()
            elif choice == 9:
                f.quit_game()
            else:
                print("Du måste ange en siffra.")
                input("Tryck på valfri tangent för att fortsätta...")

        except ValueError:
            print(
                "Du måste ange siffran som stämmer överens med det val du vill göra."
            )
            input("Tryck på valfri tangent för att fortsätta...")
            f.clear_screen()
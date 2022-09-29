import msvcrt as m
import game.user_guess as ug
import game.user_think as ut
import game.functions as f

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
    
    print("""
----------MAIN MENU----------
1. Spela som gissare    
2. Spela som tänkare
3. Se nuvarande highscore
-----------------------------
8. Återställ highscore
9. Avsluta""")

    try:
        choice = int(input("Välj ett alternativ: "))
        if choice == 1:
            ug.user_guess()
        elif choice == 2:
            ut.user_think()
        elif choice == 3:
            try:
                f.print_highscore()
            except ValueError:
                print("Det finns inga highscores än.")
            print("\nTryck på valfri tangent för att fortsätta.")
            m.getch()
            main_menu()
        elif choice == 8:
            f.reset_highscore()
        elif choice == 9:
            exit()
        else:
            print("Du måste ange siffran som stämmer överens med det val du vill göra.")
            main_menu()
    except ValueError:
        print("Vänligen ange ett giltligt alternativ.")
        main_menu()



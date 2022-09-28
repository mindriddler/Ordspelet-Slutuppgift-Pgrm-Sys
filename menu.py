import msvcrt as m
from user_think import *
from user_guess import *

def splash_screen():
    
    print("""
-----------------------------
Spelregler är som följer!
        
1. Ordet måste vara svenskt.
2. Ordet måste vara 5 bokstäver.
3. Ordet får inte vara ett namn.
4. Ordet får inte ha tempus-böjning.
5. Ordet får inte ha plural-böjning.
6. Ordet får inte ha upprepade bokstäver, så som "hemma".""")
    accept = input("\nAccepterar du spelreglerna? ").lower()
    if accept == "ja":
        main_menu()
        menu_choice()
    elif accept == "nej":
        print("Då får du inte lov att vara med och spela.\nAvslutar spelet.")
        exit()
    else:
        print("Vänligen acceptera spelreglerna för att kunna spela.\nTryck på valfri tangent för att fortsätta.")
        m.getch()
        splash_screen()


def main_menu():   
    
    print("""
----------MAIN MENU----------
1. Spela som gissare    
2. Spela som tänkare
-----------------------------
9. Avsluta""")


def menu_choice():
    try:
        choice = int(input("Välj ett alternativ: "))
        if choice == 1:
            user_guess()
        elif choice == 2:
            user_think()
    except ValueError:
        print("Vänligen ange ett giltligt alternativ.")
        menu_choice()
        
        
splash_screen()
    

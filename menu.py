import msvcrt as m
from user_think import *
from user_guess import *

def splash_screen():
    
    print("""
-----------------------------
Gamerules are as follows:
        
1. The word have to be swedish.
2. The word have to be 5 letters long.
3. The word can not be a name.
4. The word can not have tempus form.
5. The word can not have a plural form.
6. The word can not contain repeted characters, such as "sitta".""")
    accept = input("\nDo you accept the game rules?: ").lower()
    if accept == "yes":
        main_menu()
        menu_choice()
    elif accept == "no":
        print("Then you can not play this game.\nExiting the game.")
        exit()
    else:
        print("Kindly accept the game rules in order to play.\nPress any key to continue.")
        m.getch()
        splash_screen()


def main_menu():   
    
    print("""
----------MAIN MENU----------
1. Play as guesser (guess the word)  
2. Play as thinker (think of word)
-----------------------------
9. Exit""")


def menu_choice():
    try:
        choice = int(input("Choose an option: "))
        if choice == 1:
            user_guess()
        elif choice == 2:
            user_think()
        else:
            print("You need to enter either 1 or 2.")
            menu_choice()
    except ValueError:
        print("Kindly enter a number.")
        menu_choice()

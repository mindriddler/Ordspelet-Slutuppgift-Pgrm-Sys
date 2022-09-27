
import msvcrt as m
import random
from venv import create


num_of_guesses = 0
end_of_game = False

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

def get_word():
    try:
        file = open("words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = "Polis" # random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i din nuvarande mapp för att spelet ska köra.\nVänligen lägg till filen och försök igen.")
        exit()


def create_word_list():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            file_content = [word.strip() for word in file.readlines()]
        return file_content
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i din nuvarande mapp för att spelet ska köra.\nVänligen lägg till filen och försök igen.")
        exit()

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

def user_guess():
    global num_of_guesses
    global end_of_game 
    
    while not end_of_game:
        guess = input("Gissar på ett ord: ").lower()
        num_of_guesses += 1
        if len(guess) != 5:    
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == get_word().lower():
            print("Du gissade rätt!")
            print(f"Du hade totalt {num_of_guesses} gissningar.")
            end_of_game = True
        else:
            correct_position = 0
            correct_letter = 0

            for i, l in enumerate(get_word().lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            
            print(f"\n{correct_position} bokstäver på RÄTT plats!\n{correct_letter} korrekta bokstäver men på FEL plats.")
        

def user_think():
    user_word = input("Vad är ditt ord?: ")
    letter_list = list(user_word)
    my_list = create_word_list()
    print(letter_list)
    
    for l in range(letter_list):
        my_new_list = [value_str for value_str in my_list if value_str[0] != letter_list[l]]    
    print(len(my_new_list))
splash_screen()



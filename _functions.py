import random



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
        print("Vänligen acceptera spelreglerna för att kunna spela.")
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
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i din nuvarande mapp för att spelet ska köra.\nVänligen lägg till filen och försök igen.")
        exit()


def menu_choice():
    try:
        choice = int(input("Välj ett alternativ: "))
        if choice == 1:
            user_guess()
        # elif choice == 2:
            # user_think() Creating at a later stage
    except ValueError:
        print("Vänligen ange ett giltligt alternativ.")
        menu_choice()

def user_guess():
    guess = input("Gissar på ett ord: ").lower()
    if len(guess) != 5:    
        print("Vänligen ange ett giltligt ord.")
        user_guess()
    if guess == get_word().lower():
        print("Du gissade rätt!")



        
        

get_word()        
splash_screen()



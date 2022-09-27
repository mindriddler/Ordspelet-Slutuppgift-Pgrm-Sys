def menu():   
    
    return """
----------MAIN MENU----------
1. Spela som gissare    
2. Spela som tänkare
-----------------------------
9. Avsluta"""

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
    guess = input("Gissar på ett ord: ").lower()
    if len(guess) != 5:    
        print("Vänligen ange ett giltligt ord.")
        user_guess()
    if guess == get_word().lower():
        print("Du gissade rätt!")

    
    

def get_word():
    try:
        file = open("words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = "Polis" #random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("Filen måste finnas i din nuvarande mapp för att programmet ska köra.")
        exit()
        
        
        
print(menu())
get_word
menu_choice()

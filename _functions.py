def menu():   
    
    return """
----------MAIN MENU----------
1. Play as guesser
2. Play as thinker
-----------------------------
9. Exit"""

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

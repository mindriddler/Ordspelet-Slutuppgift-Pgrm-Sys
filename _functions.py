def menu():   
    
    return """
----------MAIN MENU----------
1. Play as guesser
2. Play as thinker
-----------------------------
9. Exit"""

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
        
        

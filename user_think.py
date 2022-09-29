import random
from functions_for_words import create_word_list

# Funktion för att loopa igenom tills ordlistan antigen är slut eller rätt ord är gissat
def user_think():
    
    end_of_game = False
    python_list = create_word_list()
    
    user_word = input("Vad är ditt ord?: ").lower()
    print("Du kan avsluta spelet genom att skriva 'quit'")
    
    while not end_of_game:
        
        word = random.choice(python_list)
        
        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")
        
        player_check = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if player_check == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = True
        elif player_check == "fel":
            correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
            correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
            correct_letters = int(correct_spot) + int(correct_char)
        elif player_check == "quit":
            exit()
        elif len(python_list) == 0:
            print("Python har inte fler ord kvar att gissa på.\nAvslutar spelet.")
            end_of_game = True
        else:
            print("Du måste skriva 'rätt' eller 'fel'.")
            
        if correct_letters == 0:
            python_list = [word for word in python_list if not len((set(user_word)).intersection(set(word))) == 5]
        elif correct_letters >= 1:
            python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
            if word in python_list:
                python_list.remove(word)










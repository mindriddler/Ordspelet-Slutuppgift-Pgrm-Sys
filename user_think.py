import random
from functions_for_words import create_word_list

def user_think():
    
    end_of_game = False
    python_list = create_word_list()
    
    user_word = input("What is your word?: ").lower()
    
    while not end_of_game:
        
        word = random.choice(python_list)
        print("You can quit the game at any time by typing 'quit'")
        print(f"\nYour word: {user_word}")
        print(f"Pythons guess: {word}")
        
        player_check = input("Please indicate whether the guess is correct or incorrect: ").lower()
        
        if player_check == "right":
            print("Python managed to guess the word!")
            end_of_game = True
        elif player_check == "wrong":
            correct_spot = input("How many CORRECT letter on CORRECT place?: ")
            correct_char = input("How many CORRECT letters on INCORRECT place?: ")
            correct_letters = int(correct_spot) + int(correct_char)
        elif player_check == "quit":
            exit()
        elif len(python_list) == 0:
            print("Python does not have any more words to guess.\Exiting the game.")
            end_of_game = True
        else:
            print("You need to enter either 'correct' or 'incorrect'.")
            
        if correct_letters == 0:
            python_list = [word for word in python_list if not len((set(user_word)).intersection(set(word))) == 5]
        elif correct_letters >= 1:
            python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
            if word in python_list:
                python_list.remove(word)
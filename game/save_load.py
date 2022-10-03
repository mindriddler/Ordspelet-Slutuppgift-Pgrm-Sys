import json
import os
import functions as f


def save_game(word, guessed_words, num_of_guesses):
    
    if os.path.exists('data\save_game.txt'): # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
        os.remove('data\save_game.txt') 
    try:
        with open('data\save_game.txt', 'r', encoding="utf-8") as file:
            save_game = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        save_game = []
    
    save_game.append((word, guessed_words, num_of_guesses))
    with open('data\save_game.txt', 'w', encoding="utf-8") as file:
        json.dump(save_game, file)

    print("Ditt spel har sparats!")
    
    while True:
        choice = input("Vill du fortsätta spela eller vill du avsluta spelet?: ").lower()
        if choice == "avsluta":
            f.quit_game()
        elif choice == "fortsätta":
            return False
        else:
            print("Du måste skriva 'avsluta' eller 'fortsätta'.")
            continue


def load_game():
    
    try:
        with open('data\save_game.txt', 'r', encoding="utf-8") as file:
            save_game = json.load(file)
            word = save_game[0][0]
            guessed_words = save_game[0][1]
            num_of_guesses = save_game[0][2]
            return word, guessed_words, num_of_guesses
    except FileNotFoundError:
        print("Det finns inget sparad spel att ladda.")
        return FileNotFoundError
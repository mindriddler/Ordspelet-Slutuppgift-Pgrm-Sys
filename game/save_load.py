import json
import os
import game.functions as f

def save_game(word, guessed_words, num_of_guesses):
    # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
    if os.path.exists('data\save_game.txt'): 
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
            return
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


def load_into_gm():
    
    no_game_saved = False
    while not no_game_saved:
        load = load_game()
        if load == FileNotFoundError:
            return FileNotFoundError 
        break
    
    num_of_guesses = load[2]
    word = load[0]
    guessed_words = load[1]
    return num_of_guesses, word, guessed_words   


def delete_save():
    try:
        os.remove('data\save_game.txt')
        print("Sparat spel har tagits bort.")
        input("Tryck på valfri tangent för att fortsätta...")
    except FileNotFoundError:
        print("Det finns inget sparat spel att ta bort.")
import json
import os
import game.functions as f
import msvcrt as m

def save_game(word, guessed_words, num_of_guesses):
    
    if os.path.exists('data\save_game.txt'): # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
        os.remove('data\save_game.txt')
    try:
        with open('data\save_game.txt', 'r', encoding="utf-8") as file:
            save_game = json.load(f)
    except FileNotFoundError:
        # If the file does not exist, use default values
        save_game = []
    
    save_game.append((word, guessed_words, num_of_guesses))
    with open('data\save_game.txt', 'w', encoding="utf-8") as file:
        json.dump(save_game, file)

    print("Your game has been saved!")
    
    while True:
        choice = input("Do you want to continue playing or do you want to end the game?: ").lower()
        if choice == "exit":
            f.quit_game()
        elif choice == "continue":
            return False
        else:
            print("You must type 'quit' or 'continue'.")
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
        print("There is no save game to load.")
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
        print("Saved game has been deleted.")
        print("Press any key to continue.")
        m.getch()
    except FileNotFoundError:
        print("There is no save game to delete.")
import json
import os
import game.functions as f


def save_game_gm1(word, guessed_words, num_of_guesses):
    # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
    if os.path.exists('data\save_game_1.txt'):
        os.remove('data\save_game_1.txt')
    try:
        with open('data\save_game_1.txt', 'r', encoding="utf-8") as file:
            save_game = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        save_game = []

    save_game.append((word, guessed_words, num_of_guesses))
    with open('data\save_game_1.txt', 'w', encoding="utf-8") as file:
        json.dump(save_game, file)
    print("Ditt spel har sparats!")

    while True:
        choice = input(
            "Vill du fortsätta spela eller vill du avsluta spelet?: ").lower()
        if choice == "avsluta":
            f.quit_game()
        elif choice == "fortsätta":
            return
        else:
            print("Du måste skriva 'avsluta' eller 'fortsätta'.")
            continue


def save_game_gm2(user_word, python_list, num_of_turns):
    # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
    if os.path.exists('data\save_game_2.txt'):
        os.remove('data\save_game_2.txt')
    try:
        with open('data\save_game_2.txt', 'r', encoding="utf-8") as file:
            save_game = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        save_game = []

    save_game.append((user_word, python_list, num_of_turns))
    with open('data\save_game_2.txt', 'w', encoding="utf-8") as file:
        json.dump(save_game, file)
    print("Ditt spel har sparats!")

    while True:
        choice = input(
            "Vill du fortsätta spela eller vill du avsluta spelet?: ").lower()
        if choice == "avsluta":
            f.quit_game()
        elif choice == "fortsätta":
            return
        else:
            print("Du måste skriva 'avsluta' eller 'fortsätta'.")
            continue


def load_game(save_file):

    try:
        if save_file == 'data\save_game_1.txt':
            with open(save_file, 'r', encoding="utf-8") as file:
                save_game = json.load(file)
                word = save_game[0][0]
                guessed_words = save_game[0][1]
                num_of_guesses = save_game[0][2]
                return num_of_guesses, word, guessed_words
        elif save_file == 'data\save_game_2.txt':
            with open(save_file, 'r', encoding="utf-8") as file:
                save_game = json.load(file)
                user_word = save_game[0][0]
                python_list = save_game[0][1]
                num_of_turns = save_game[0][2]
                return user_word, python_list, num_of_turns
    except FileNotFoundError:
        print("Det finns inget sparad spel att ladda.")
        input("Tryck på valfri tangent för att fortsätta...")
        f.clear_screen()
        return FileNotFoundError


def delete_save(save_file):
    try:
        os.remove(save_file)
        print("Sparat spel har tagits bort.")
        input("Tryck på valfri tangent för att fortsätta...")
        f.clear_screen()
    except FileNotFoundError:
        print("Det finns inget sparat spel att ta bort.")
        input("Tryck på valfri tangent för att fortsätta...")
        f.clear_screen()
import json
from operator import itemgetter
import game.functions as f
from itertools import islice
import os

def highscore(num_of_guesses):
    
    while True:
        choice = input("Do you want to save your highscore?: ").lower()
        if choice == "yes":
            name = input("Please write your full name: ").title()
            try:
                with open('data\highscore.txt', 'r') as file:
                    highscores = json.load(file)
            except FileNotFoundError:
                # If the file doesn't exist, use default values
                highscores = []
        
            highscores.append((name, num_of_guesses))
            highscores = sorted(highscores, key = itemgetter(1), reverse = False)[:10]
            with open('data\highscore.txt', 'w') as file:
                json.dump(highscores, file)

            highscores = []
            print("Your score has been saved!")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif choice == "no":
            print("Your score has not been saved.")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif choice == "quit":
            f.quit_game()
        else:
            print("You need to type 'yes' or 'no'.\nType 'quit' to quit the game.")
            continue


def print_highscore():
    
    try:
        with open('data\highscore.txt', 'r') as file:
            highscores = json.load(file)
            limit = 10
        print("\nCurrent highscore!")
        for item in islice(highscores, limit):
            print(f"{item[0]}: {item[1]} guesses")
    except FileNotFoundError:
        print("There is no highscore yet. Play the game to save your score.")
    try:
        average_guesses = sum([item[1] for item in highscores]) / len(highscores)
        print(f"\nAverge of how many guesses: {average_guesses}")
    except UnboundLocalError:
        pass


def reset_highscore():
    reset_done = False
    
    while not reset_done:
        password = input("Enter password: ").lower()
        if password == "qwerty123":
            additional_check = input("Are you sure you want to reset the highscores?: ").lower()
            if additional_check == "yes":
                if os.path.exists('data\highscore.txt'):
                    os.remove('data\highscore.txt')
                    print("Highscore has been reset!\nReturns to main menu.")
                    reset_done = True
                else:
                    print("There is currently no highscore saved. Can't reset.\nReturns to main menu.")
                    reset_done = True
            elif additional_check == "no":
                print("Returns to main menu.")
                reset_done = True
            elif additional_check == "quit":
                f.quit_game()
            else:
                print("You need to type 'yes' or 'no'.")
                continue
        elif password == "main menu":
            print("Returns to main menu.")
            reset_done = True
        elif password == "quit":
            f.quit_game()
        else:
            print("Wrong password. Try again or return to the main menu by typing 'main menu'.")
            continue
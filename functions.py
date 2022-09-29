from itertools import islice
import random
import json
from operator import itemgetter

import menu


def get_word():
    try:
        file = open("words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i din nuvarande mapp för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        exit()


def create_word_list():
    try:
        with open("words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i din nuvarande mapp för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        exit()
        

def highscore(name, num_of_guesses):
    try:
        with open('highscore.txt', 'r') as f:
            highscores = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        highscores = []
    
    highscores.append((name, num_of_guesses))
    highscores = sorted(highscores, key = itemgetter(1), reverse = False)[:10]
    with open('highscore.txt', 'w') as f:
        json.dump(highscores, f)

    highscores = []
    print("Din poäng har sparats!")
    play_again = input("Vill du spela igen?: ").lower()
    if play_again == "ja":
        menu.main_menu()
    elif play_again == "nej":
        print("Avslutar spelet.")
        exit()
    else:
        print("Du måste ange 'ja' eller 'nej'.")

def print_highscore():
    with open('highscore.txt', 'r') as f:
        highscores = json.load(f)
        limit = 10
    print("\nNuvarande toplista!")
    for item in islice(highscores, limit):
        print(f"{item[0]}: {item[1]} gissningar")
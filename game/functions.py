import os
from itertools import islice
import random
import json
from operator import itemgetter
import game.menu as menu


def get_word():
    try:
        file = open("data\words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        exit()


def create_word_list():
    try:
        with open("data\words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
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
    play_again_func()


def play_again_func():   
    play_again = input("\nVill du återvända till huvudmenyn?: ").lower()
    if play_again == "ja":
        menu.main_menu()
    elif play_again == "nej":
        print("\nAvslutar spelet.\nHa en bra dag!")
        exit()
    else:
        print("\nDu måste ange 'ja' eller 'nej'.")
        play_again_func()


def print_highscore():
    with open('data\highscore.txt', 'r') as f:
        highscores = json.load(f)
        limit = 10
    print("\nNuvarande topp 10 bästa spelrundor!")
    for item in islice(highscores, limit):
        print(f"{item[0]}: {item[1]} gissningar")
        
    average_guesses = sum([item[1] for item in highscores]) / len(highscores)
    print(f"\nMedelvärdet på antal gissningar är: {average_guesses}")
    
def reset_highscore():
    password = input("Ange lösenord: ").lower()
    if password == "qwerty123":
        additional_check = input("Är du säker på att du vill återställa highscoren?: ").lower()
        if additional_check == "ja":
            if os.path.exists('data\highscore.txt'):
                os.remove('data\highscore.txt')
                print("Highscore har nollställts!\nÅtergår till huvucmenyn.")
                menu.main_menu()
            else:
                print("Det finns förnärvarande inget highscore sparat. Kan inte återställa.\nÅtergår till huvudmenyn.")
                menu.main_menu()
        elif additional_check == "nej":
            print("Återgår till huvudmenyn.")
            menu.main_menu()
    elif password == "huvudmeny":
        print("Återgår till huvudmenyn.")
        menu.main_menu()
    else:
        print("Fel lösenord. Försök igen eller återgå till huvudmenyn genom att skriva 'huvudmeny'.")
        reset_highscore()
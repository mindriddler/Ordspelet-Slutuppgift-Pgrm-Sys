import os
from itertools import islice
import random
import json
from operator import itemgetter


def game_func_1():
    num_of_guesses = 0
    end_of_game = False
    word = get_word()
    guessed_words = []
        
    print("Du kan avsluta spelet genom att skriva 'quit'")
        
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1


        if guess == "quit":
            print("Avslutar spelet.\nHa en bra dag!")
            exit()
        elif len(guess) != 5:    
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == word.lower():
            print("Du gissade rätt!")
            if num_of_guesses == 1:
                print(f"Du hade totalt {num_of_guesses} gissning.\n")
            else:
                print(f"Du hade totalt {num_of_guesses} gissningar.\n")
            choice = input("Vill du skriva in dig på toplistan?: ").lower()
            if choice == "ja":
                name = input("Vänligen ange ditt fulla namn: ").title()
                end_of_game = True
                highscore(name, num_of_guesses)
            elif choice == "nej":
                play_again = input("Vill du återvända till huvudmenyn?: ").lower()
                if play_again == "ja":
                    end_of_game = True
                elif play_again == "nej":
                    print(f"Avslutar spelet.\nHa en bra dag!")
                    end_of_game = True
                else:
                    print("Du måste ange 'ja' eller 'nej'.")
        elif guess in guessed_words:
            print("Du har redan gissat på det ordet. Prova med ett annat ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        else:
            guessed_words.append(guess)
            for i, l in enumerate(word.lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            print(f"\n{correct_position} bokstäver på RÄTT plats!\n{correct_letter} korrekta bokstäver men på FEL plats.")


def game_func_2():
    
    python_list, num_of_turns, end_of_game, user_word = player_word()
    while not end_of_game:
        python_list, word, user_word, player_check, num_of_turns, end_of_game = main_func(python_list, num_of_turns, end_of_game, user_word)
        python_list, num_of_turns, end_of_game, user_word = checking(python_list, word, user_word, player_check, num_of_turns, end_of_game)
            
    print(f"Du klarade det på {num_of_turns} försök.")
    print("Tack för att du spelade!")
    exit()


def player_word():    
    
    end_of_game = False
    python_list = create_word_list()
    num_of_turns = 0
    
    while True:
        user_word = input("Vad är ditt ord?: ").lower()
        if len(user_word) != 5:
            print("Du måste ange ett giltligt ord.")
        elif user_word.isalpha() == False:
            print("Ordet får inte innehålla nummer eller andra symboler.")
        else:
            print("Du kan avsluta spelet genom att skriva 'quit'")
            return python_list, num_of_turns, end_of_game, user_word
        
        
def main_func(python_list, num_of_turns, end_of_game, user_word): 
    
    while not end_of_game:
        num_of_turns += 1
        if num_of_turns % 5 == 0:
            choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower() # Utökning av programmet som PDF filen föreslagit
            if choice == "ja":
                print(python_list)
                print(f"Python har {len(python_list)} kvar att gissa på.")
            else:
                pass
        try:
            word = random.choice(python_list)
        except IndexError:
            print("Python har inte fler ord kvar att gissa på.\nAvslutar spelet.")
            exit()
            
        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")

        player_check = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if player_check == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = True
        elif player_check == "fel":
            return python_list, word, user_word, player_check, num_of_turns, end_of_game
            


def checking(python_list, word, user_word, player_check, num_of_turns, end_of_game):     
    
    while True:
        correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
        correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
        
        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("Du måste skriva in siffror. Försök igen.")
            continue
        else:
            pass
        
        correct_letters = int(correct_spot) + int(correct_char)
        
        if player_check == "quit":
            print("Avslutar spelet.")
            exit()
        elif correct_letters == 0:
            python_list = [word for word in python_list if not len(set(user_word).intersection(set(word))) == 5]
        elif correct_letters >= 1:
            python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
            if word in python_list:
                python_list.remove(word)
        return python_list, num_of_turns, end_of_game, user_word


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
        with open('data\highscore.txt', 'r') as f:
            highscores = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        highscores = []
    
    highscores.append((name, num_of_guesses))
    highscores = sorted(highscores, key = itemgetter(1), reverse = False)[:10]
    with open('data\highscore.txt', 'w') as f:
        json.dump(highscores, f)

    highscores = []
    print("Din poäng har sparats!")


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
    reset_done = False
    
    while not reset_done:
        password = input("Ange lösenord: ").lower()
        if password == "qwerty123":
            additional_check = input("Är du säker på att du vill återställa highscoren?: ").lower()
            if additional_check == "ja":
                if os.path.exists('data\highscore.txt'):
                    os.remove('data\highscore.txt')
                    print("Highscore har nollställts!\nÅtergår till huvucmenyn.")
                    reset_done = True
                else:
                    print("Det finns förnärvarande inget highscore sparat. Kan inte återställa.\nÅtergår till huvudmenyn.")
                    reset_done = True
            elif additional_check == "nej":
                print("Återgår till huvudmenyn.")
                reset_done = True
        elif password == "huvudmeny":
            print("Återgår till huvudmenyn.")
            reset_done = True
        else:
            print("Fel lösenord. Försök igen eller återgå till huvudmenyn genom att skriva 'huvudmeny'.")
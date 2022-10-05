import os
import random
import game.hint_functions as h_f

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


def return_to_main_menu():
    while True:
        go_back = input("Vill du återvända till huvudmenyn?: ").lower()
        if go_back == "ja":
            end_of_game = True
            return end_of_game
        elif go_back == "nej":
            quit_game()
        else:
            print("Du måste ange 'ja' eller 'nej'.")
            continue


def remove_hints():
    try:    
        if os.path.exists('data\hints.txt'):
            os.remove('data\hints.txt')
    except PermissionError:
        pass


def quit_game():
    print("Avslutar spelet.\nHa en bra dag!")
    remove_hints()
    exit()


def player_word():    
    
    while True:
        user_word = input("Vad är ditt ord?: ").lower()
        to_many_l = 0
        
        for char in user_word:
            count = user_word.count(char)
            if count > 1:
                to_many_l = count
                break
        
        if to_many_l > 1:
            print("Ditt ord innehåller dubletter. Vänligen ange ett giltligt ord.\n")
        elif len(user_word) != 5:
            print("Du måste ange ett giltligt ord.")
        elif user_word.isalpha() == False:
            print("Ordet får inte innehålla nummer eller andra symboler.\n")
        else:
            print("Du kan avsluta spelet genom att skriva 'quit'.")
            return user_word


def create_word_list():
    try:
        with open("data\words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        exit()


def add_word_to_words(word):
    
    print("""\nDu verkar inte ha gjort några fel med dina ledtrådar.
Därför har jag kommit fram till att ditt ord saknas i ordlistan
och kommer därför lägga till det för framtida spel.
Tack för ditt bidrag!\n""")
    try:
        with open('data\words.txt', 'a+', encoding="utf-8") as f:
            f.write("\n" + word)
    except FileNotFoundError:
        print("Kunde inte hitta ordlistan. Kan inte lägga till ordet.")
        return FileNotFoundError


def check_pos(guess, word):
    
    while True:
        correct_position = 0
        correct_letter = 0
    
        for i, l in enumerate(word.lower()):
            if l == guess[i]:
                correct_position += 1
            elif l in guess:
                correct_letter += 1
        return correct_position, correct_letter
    

def correlation(correct_spot, correct_char, python_list, word, user_word):
    
    correct_letters = int(correct_spot) + int(correct_char)
            
    if correct_letters == 0:
        python_list = [word for word in python_list if not len(set(user_word).intersection(set(word))) == 5]
    elif correct_letters >= 1:
        python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
        if word in python_list:
            python_list.remove(word)
    return python_list


def check_if_word_valid(guess, guessed_words):
    
    to_many_l = 0
    
    for char in guess:
            count = guess.count(char)
            if count > 1:
                to_many_l = count
                break
    
    if to_many_l > 1 or len(guess) != 5 or guess.isalpha() == False:
        print("Ditt ord är inte ett giltligt ord. Kontrollera och välj ett nytt.")
        return "not valid"
    elif guess in guessed_words:
        print("Du har redan gissat på det ordet. Prova med ett annat ord.")
        return "not valid"
    else:
        return "valid"


def checking(python_list, word, user_word):    
    
    while True:
        correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
        correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("Du måste skriva in siffror. Försök igen.")
            continue
        elif correct_char == "quit" or correct_spot == "quit":
            quit_game()
        elif int(correct_spot) + int(correct_char) > 5:
            print("\nDu måste ha angivit fel siffror. Försök igen.")
            continue
        else:
            h_f.save_hint(word, user_word, correct_spot, correct_char)
            return correlation(correct_spot, correct_char, python_list, word, user_word)
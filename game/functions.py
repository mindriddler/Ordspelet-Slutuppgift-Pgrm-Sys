import os
import random

def get_word():
    try:
        file = open("data\words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("The file 'words.txt' have to be in the data folder in order for the game to work.\nKindly add the file and try again.")
        exit()


def return_to_main_menu():
    while True:
        go_back = input("Do you want to return to the main menu?: ").lower()
        if go_back == "yes":
            end_of_game = True
            return end_of_game
        elif go_back == "no":
            quit_game()
        else:
            print("You need to type 'yes' or 'no'.")
            continue


def remove_hints():
    try:    
        if os.path.exists('data\hints.txt'):
            os.remove('data\hints.txt')
    except PermissionError:
        pass


def quit_game():
    print("Exiting the game.\nHave a good day!")
    remove_hints()
    exit()


def player_word():    
    
    while True:
        user_word = input("What is your word?: ").lower()
        to_many_l = 0
        
        for char in user_word:
            count = user_word.count(char)
            if count > 1:
                to_many_l = count
                break
        
        if to_many_l > 1:
            print("The word contains duplicates. Kindly choose another word.\n")
        elif len(user_word) != 5:
            print("The word has to bee 5 letters. Kindly choose another word.\n")
        elif user_word.isalpha() == False:
            print("The word can not contain numbers or symbols. Kindly choose another word.\n")
        else:
            print("You can quit the game by typing 'quit'.")
            return user_word


def create_word_list():
    try:
        with open("data\words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("The file 'words.txt' have to be in the data folder in order for the game to work.\nKindly add the file and try again.")
        exit()


def add_word_to_words(word):
    
    print("""\You don't seem to have made any mistakes with your clues.
Therefore, I have come to the conclusion that your word is missing from the dictionary
and will therefore add it for future games.
Thank you for your contribution!\n""")
    try:
        with open('data\words.txt', 'a+', encoding="utf-8") as f:
            f.write("\n" + word)
    except FileNotFoundError:
        print("Can not find the file 'words.txt'. Can not add the word.")
        return FileNotFoundError



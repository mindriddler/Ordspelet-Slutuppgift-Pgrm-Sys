import random

def get_word():
    try:
        file = open("words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print("The file 'words.txt' must be in your current folder for the game to work.\nPlease add the file and try again.")
        exit()


def create_word_list():
    try:
        with open("words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("The file 'words.txt' must be in your current folder for the game to work.\nPlease add the file and try again.")
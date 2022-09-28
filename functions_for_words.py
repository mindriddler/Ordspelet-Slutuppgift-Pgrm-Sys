import random

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
import random


# To get a random word from the txt file
def get_word():
    
    file = open("words_utf.txt", "r", encoding="utf-8")
    words = file.read()
    listOfWords = words.split("\n")
    randWord = random.choice(listOfWords)
    return randWord



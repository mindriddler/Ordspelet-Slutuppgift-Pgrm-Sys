import os
from itertools import islice
import random
import json
from operator import itemgetter


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


def quit_game():
    print("Avslutar spelet.\nHa en bra dag!")
    exit()


def game_func_1():
    num_of_guesses = 0
    end_of_game = False
    word = get_word()
    guessed_words = []
        
    print("Du kan avsluta spelet genom att skriva 'jag ger upp'.")   
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1


        if guess == "jag ger upp":
            print(f"Ordet var {word}")
            quit_game()
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
            end_of_game = highscore(num_of_guesses)
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
    
    end_of_game = False
    num_of_turns = 0
    user_word = player_word()
    python_list = create_word_list()
    
    
    while not end_of_game:
        
        try:
            num_of_turns += 1
            word = random.choice(python_list)
            answer = main_func(python_list, user_word, word, num_of_turns)
            
            if answer == "fel":
                python_list = checking(python_list, word, user_word)
            elif answer == "quit":
                quit_game()
            elif answer == None:
                end_of_game = True
            else:
                print("Du måste ange 'rätt' eller 'fel'.")
                continue
        except TypeError:
            end_of_game = True


def player_word():    
    
    while True:
        user_word = input("Vad är ditt ord?: ").lower()
        if len(user_word) != 5:
            print("Du måste ange ett giltligt ord.")
        elif user_word.isalpha() == False:
            print("Ordet får inte innehålla nummer eller andra symboler.")
        else:
            print("Du kan avsluta spelet genom att skriva 'quit'")
            return user_word


def main_func(python_list, user_word, word, num_of_turns):
    
    end_of_game = False
    
    while not end_of_game:
        
        try:
            if num_of_turns % 5 == 0:
                choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower() # Utökning av programmet som PDF filen föreslagit
                if choice == "ja":
                    print(python_list)
                    print(f"Python har {len(python_list)} kvar att gissa på.")
                else:
                    pass
        except IndexError:
            print("Python har inte fler ord kvar att gissa på.\nAvslutar spelet.")
            exit()
            
        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")

        answer = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if answer == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = return_to_main_menu()
        else:
            return answer  


def checking(python_list, word, user_word):    
    
    while True:
        correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
        correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
        
        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("Du måste skriva in siffror. Försök igen.")
            continue
        elif correct_char == "quit" or correct_spot == "quit":
            quit_game()
        else:
            pass
        
        correct_letters = int(correct_spot) + int(correct_char)
        
        if correct_letters == 0:
            python_list = [word for word in python_list if not len(set(user_word).intersection(set(word))) == 5]
        elif correct_letters >= 1:
            python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
            if word in python_list:
                python_list.remove(word)
        return python_list


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


def highscore(num_of_guesses):
    
    while True:
        choice = input("Vill du spara ditt resultat i highscore listan?: ").lower()
        if choice == "ja":
            name = input("Vänligen ange ditt fulla namn: ").title()
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
            end_of_game = return_to_main_menu()
            return end_of_game
        elif choice == "nej":
            print("Din poäng har inte sparats.")
            end_of_game = return_to_main_menu()
            return end_of_game
        elif choice == "quit":
            quit_game()
        else:
            print("Du måste ange 'ja' eller 'nej'.")
            continue


def print_highscore():
    
    try:
        with open('data\highscore.txt', 'r') as f:
            highscores = json.load(f)
            limit = 10
        print("\nNuvarande topp 10 bästa spelrundor!")
        for item in islice(highscores, limit):
            print(f"{item[0]}: {item[1]} gissningar")
    except FileNotFoundError:
        print("Det finns ingen sparad poäng än. Spela spelet för att spara din poäng.")  
    try:
        average_guesses = sum([item[1] for item in highscores]) / len(highscores)
        print(f"\nMedelvärdet på antal gissningar är: {average_guesses}")
    except UnboundLocalError:
        pass


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
            elif additional_check == "quit":
                quit_game()
            else:
                print("Du måste ange 'ja' eller 'nej'.")
                continue
        elif password == "huvudmeny":
            print("Återgår till huvudmenyn.")
            reset_done = True
        elif password == "quit":
            quit_game()
        else:
            print("Fel lösenord. Försök igen eller återgå till huvudmenyn genom att skriva 'huvudmeny'.")
            continue
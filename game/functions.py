
from doctest import ELLIPSIS_MARKER
import msvcrt as m
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


def remove_hints():
    if os.path.exists('data\hints.txt'):
        os.remove('data\hints.txt')


def quit_game():
    print("Avslutar spelet.\nHa en bra dag!")
    remove_hints()
    exit()


def game_func_1(): # Gamemode 1, player vs computer
    num_of_guesses = 0
    end_of_game = False
    word = get_word()
    guessed_words = []
        
    print("Du kan avsluta spelet genom att skriva 'jag ger upp'.")   
    print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
    
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1
        
        for char in guess:
            count = guess.count(char)
            if count > 1:
                to_many_l = count
                break
            
        if guess == "spara spelet":
            num_of_guesses -= 1 # The guess is not counted if the user saves the game
            save_game(word, guessed_words, num_of_guesses)
        elif num_of_guesses % 5 == 0:
            print("Du kan avsluta spelet genom att skriva 'jag ger upp'.") # To make sure the user knows how to quit the game. Good to have if the user forgets.
            print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
        elif guess == "jag ger upp":
            print(f"Ordet var {word}")
            quit_game()
        elif to_many_l > 1:
            print("Ditt ord innehåller dubletter. Vänligen ange ett giltligt ord.")
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


def game_func_3(): # Load feature for gamemode 1
    
    no_game_saved = False
    while not no_game_saved:
        load = load_game()
        if load == FileNotFoundError:
            no_game_saved = True
            return no_game_saved 
    
    
    num_of_guesses = load[2]
    end_of_game = False
    word = load[0]
    guessed_words = load[1]
        
    print("Du kan avsluta spelet genom att skriva 'jag ger upp'.")   
    print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
    
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1
        for char in guess:
            count = guess.count(char)
            if count > 1:
                to_many_l = count
                break
            
        if guess == "spara spelet":
            num_of_guesses -= 1 # The guess is not counted if the user saves the game
            save_game(word, guessed_words, num_of_guesses)
        elif num_of_guesses % 5 == 0:
            print("Du kan avsluta spelet genom att skriva 'jag ger upp'.") # To make sure the user knows how to quit the game. Good to have if the user forgets.
            print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
        elif guess == "jag ger upp":
            print(f"Ordet var {word}")
            quit_game()
        elif to_many_l > 1:
            print("Ditt ord innehåller dubletter. Vänligen ange ett giltligt ord.")
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


def game_func_2(): # Gamemode 2, computer vs player
    
    end_of_game = False
    num_of_turns = 0
    user_word = player_word()
    python_list = create_word_list()
    
    while not end_of_game:
        
        try:
            num_of_turns += 1
            word = random.choice(python_list)
            answer = main_func_gamemode_2(python_list, user_word, word, num_of_turns)
            
            if answer == "fel":
                python_list = checking(answer, python_list, word, user_word)
                
            elif answer == "quit":
                quit_game()
            elif answer == None:
                end_of_game = True
            else:
                print("Du måste ange 'rätt' eller 'fel'.")
                continue
        except TypeError:
            end_of_game = True
        except IndexError:
            print("\nPython har inte fler ord kvar att gissa på. Kontrollerar gissningar.")
            print("Tryck på valfri tangent för att fortsätta.")
            m.getch()
            end_of_game = get_hints()
            end_of_game = True

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
            print("Du kan avsluta spelet genom att skriva 'quit'")
            return user_word


def main_func_gamemode_2(python_list, user_word, word, num_of_turns):
    
    end_of_game = False
    
    while not end_of_game:
        
        try:
            if num_of_turns % 5 == 0:
                print("\nDu kan avsluta spelet genom att skriva 'quit'")
                choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower() # Utökning av programmet som PDF filen föreslagit
                if choice == "ja":
                    print(python_list)
                    print(f"Python har {len(python_list)} kvar att gissa på.")
                elif choice == "quit":
                    quit_game()
                else:
                    pass
        except IndexError:
            print("\nPython har inte fler ord kvar att gissa på.\nKontrollerar gissningar.\n")
            
            
        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")

        answer = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if answer == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = return_to_main_menu()
        elif answer == "fel":
            return answer
        elif answer == "quit":
            quit_game()
        else:
            print("Du måste ange 'rätt' eller 'fel'.")
            continue


def checking(answer, python_list, word, user_word):    
    
    
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
        save_hint(answer, word, user_word, correct_spot, correct_char)
        return python_list


def save_hint(answer, word, user_word, correct_spot, correct_char):        
    
    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as f:
            hint_list = json.load(f)
    except FileNotFoundError:
    # If the file doesn't exist, use default values
        hint_list = []
        
    hint_list.append((answer, word, user_word, correct_spot, correct_char))
    with open('data\hints.txt', 'w', encoding="utf-8") as f:
        json.dump(hint_list, f)
        

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


def save_game(word, guessed_words, num_of_guesses):
    
    if os.path.exists('data\save_game.txt'): # If the file exists, delete it before saving the new game. Right now the save feature only saves one game at a time.
        os.remove('data\save_game.txt') 
    try:
        with open('data\save_game.txt', 'r', encoding="utf-8") as f:
            save_game = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        save_game = []
    
    save_game.append((word, guessed_words, num_of_guesses))
    with open('data\save_game.txt', 'w', encoding="utf-8") as f:
        json.dump(save_game, f)

    print("Ditt spel har sparats!")
    
    while True:
        choice = input("Vill du fortsätta spela eller vill du avsluta spelet?: ").lower()
        if choice == "avsluta":
            quit_game()
        elif choice == "fortsätta":
            return False
        else:
            print("Du måste skriva 'avsluta' eller 'fortsätta'.")
            continue


def load_game():
    
    try:
        with open('data\save_game.txt', 'r', encoding="utf-8") as f:
            save_game = json.load(f)
            word = save_game[0][0]
            guessed_words = save_game[0][1]
            num_of_guesses = save_game[0][2]
            return word, guessed_words, num_of_guesses
    except FileNotFoundError:
        print("Det finns inget sparad spel att ladda.")
        return FileNotFoundError
    

def add_word_to_words(word):
    
    print("""\nDu verkar inte ha gjort några fel med dina ledtrådar.
Därför har jag kommit fram till att ditt ord saknas i ordlistan
och kommer därför lägga till det för framtida spel.
Tack för ditt bidrag!\n""")

    try:
        with open('data\words.txt', 'r', encoding="utf-8") as f:
            words = json.load(f)
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        
    words.append(word)
    with open('data\words.txt', 'w', encoding="utf-8") as f:
        json.dump(words, f)
        
        print("Ordet har lagts till i ordlistan!")
        print("Tryck på valfri tangent för att återgå till huvudmenyn.")
        m.getch()
        end_of_game = True
        return end_of_game


def get_hints():
    word_list = create_word_list()
    correct_position = 0
    correct_letter = 0
    to_many_l = 0
    hint_no = 0
    word = input("\nVad var ditt ord? ").lower()
    
    
        
    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as f:
            hints = json.load(f)
            len_hints = len(hints)
                    
            for r in range(len_hints):
                        
                hint = hints[r]
                hint_no = r + 1
                python_guess = hint[1]
                user_word = hint[2]
                correct_spot = hint[3]
                correct_char = hint[4]

                for char in word:
                    count = word.count(char)
                    if count > 1:
                        to_many_l = count
                            
                if word == "visa mitt ord":
                    print(f"Ordet var '{user_word}'.")
                    print("Tryck på valfri tangent för att fortsätta kontrollen.\n")
                    m.getch()
                elif to_many_l > 1:
                    print("Ditt ord innehåller dubletter.\nOch det är därför python inte kunnat gissa ditt ord.\n")
                    end_of_game = True
                    return end_of_game
                elif len(word) != 5:
                    print("Du måste ange ett giltligt ord.")
                    break
                elif word.isalpha() == False:
                    print("Ordet får inte innehålla nummer eller andra symboler.\n")
                elif word != user_word:
                    print("Ordet du angav stämmer inte överens med det ordet du angav när du startade spelet.")
                    print("Om du har glömt bort ditt ord, skriv: 'visa mitt ord'.")
                    print("Tryck på valfri tangent för att fortsätta.")
                    m.getch()
                    break
                else:
                    check_hints(user_word, python_guess, correct_spot, correct_char, hint_no, word, word_list)
    except FileNotFoundError:
        print("Filen 'hints.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")             



def check_hints(user_word, python_guess, correct_spot, correct_char, hint_no, word, word_list):
    if user_word == python_guess:
        print("Python gissade på rätt ord men du angav att det var fel ord!\nVänligen ha bättre översikt nästa gång.")
        print("Tryck på valfri tangent för att återvända till huvudmenyn")
        m.getch()
        end_of_game = True
        return end_of_game
    
    correct_position = 0
    correct_letter = 0
    
    for i, l in enumerate(user_word.lower()):
        if l == python_guess[i]:
            correct_position += 1
        elif l in python_guess:
            correct_letter += 1    
        
    if correct_position != correct_spot or correct_letter != correct_char:
        print(f"\nPython har gissat på ordet: '{python_guess}'")
        print(f"På gissning {hint_no} har du har svarat att det var {correct_spot} rätt bokstäver på rätt plats och {correct_char} rätt bokstäver på fel plats.")
        print(f"När det egentligen är {correct_position} rätt bokstäver på rätt plats och {correct_letter} rätt bokstäver på fel plats.")
        print("Du har alltså svarat fel på ditt svar.")
        print("Tryck på valfri tangent för att återgå till huvudmenyn.")
        correct_position = 0
        correct_letter = 0
        m.getch()
    else:
        if correct_position == correct_spot and correct_letter == correct_char:
            print(f"Du har svarat att det var {correct_position} rätt bokstäver på rätt plats och {correct_letter} rätt bokstäver på fel plats.")
            print("Du har alltså svarat rätt på ditt svar. Bra jobbat!\n")
            correct_position = 0
            correct_letter = 0
            if word not in word_list:
                end_of_game = add_word_to_words(word, word_list)
                return end_of_game

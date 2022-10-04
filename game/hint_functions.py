import json
import msvcrt as m
import game.functions as f


def save_hint(word, user_word, correct_spot, correct_char):        
    
    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as f:
            hint_list = json.load(f)
    except FileNotFoundError:
    # If the file doesn't exist, use default values
        hint_list = []
        
    hint_list.append((word, user_word, correct_spot, correct_char))
    with open('data\hints.txt', 'w', encoding="utf-8") as f:
        json.dump(hint_list, f)


def get_hints(user_word):
    
    word_list = f.create_word_list()
    to_many_l = 0
    end_of_game = False
    
    while True:
        word = input("\nWhat was your word?: ").lower()
        if word == "show my word":
            print(f"The word was '{user_word}'.")
            print("Press any key to continue the check.")
            m.getch()
        elif user_word != word:
            print("The word you supplied does not match the word you supplied when you started the game.\nIf you have forgotten your word, type 'show my word'.")
        else:
            break
    
    while not end_of_game:
        try:
            with open('data\hints.txt', 'r', encoding="utf-8") as file:
                hints = json.load(file)
                len_hints = len(hints)
                        
                for r in range(len_hints):
                    hint = hints[r]
                    python_guess = hint[0]
                    user_word = hint[1]
                    correct_spot = int(hint[2])
                    correct_char = int(hint[3])
                    
                    for char in word:
                        count = word.count(char)
                        if count > 1:
                            to_many_l = count
                            if to_many_l > 1:
                                print("Your word contains duplicates.\nAnd thats why python did not manage to guess it.\n")
                                end_of_game = f.return_to_main_menu()
                                return end_of_game
                    if len(word) != 5:
                        print("The words has to be 5 letters.")
                        break
                    elif word.isalpha() == False:
                        print("The word can not contain number or symbols.\n")  
                    else:
                        corr_or_wrong = check_hints(user_word, python_guess, correct_spot, correct_char, len_hints, hints)
                    
                    if corr_or_wrong == "wrong":
                        end_of_game = f.return_to_main_menu()
                        return end_of_game
                    elif corr_or_wrong == "correct":
                        if word not in word_list:
                            end_of_game = f.add_word_to_words(word)
                            return end_of_game
                    else:
                        return end_of_game
        except FileNotFoundError:
            print("The file 'hints.txt' does not exist.\nCan not check hints.\nReturning to main menu.")


def check_hints(user_word, python_guess, correct_spot, correct_char, len_hints, hints):

    correct_position = 0
    correct_letter = 0
    correct_hints = 0
    wrong_hints = 0
    
    for r in range(len_hints):
        hint = hints[r]
        python_guess = hint[0]
        if user_word == python_guess:
            print("\nPython actually guessed the correct word but you have indicated that it was wrong.\nPlease double check your input and try again.\n")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        continue
    for i, l in enumerate(user_word.lower()):
        if l == python_guess[i]:
            correct_position += 1
        elif l in python_guess:
            correct_letter += 1    
            
    if correct_position != correct_spot or correct_letter != correct_char:
        wrong_hints += 1
    elif correct_position == correct_spot and correct_letter == correct_char:
        correct_hints += 1
        
    if wrong_hints > 0:
        print(f"\nYou have entered the wrong number of correct positions or correct letters in {wrong_hints} of your hints.\nPlease check your entries better and try again.")
        print("Press any key to continue.\n")
        return "wrong"
    elif correct_hints > 0:
        print(f"\nYou have entered the correct number of correct positions and correct letters in the {correct_hints} of your hints.\nGood job!")
        print("Press any key to continue.\n")
        return "correct"
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
        word = input("\nVad var ditt ord?: ").lower()
        if word == "visa mitt ord":
            print(f"Ordet var '{user_word}'.")
            print("Tryck på valfri tangent för att fortsätta kontrollen.")
            m.getch()
        elif user_word != word:
            print("Ordet du angav stämmer inte överens med det ordet du angav när du startade spelet. \nOm du har glömt bort ditt ord, skriv: 'visa mitt ord'.")
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
                                print("Ditt ord innehåller dubletter.\nOch det är därför python inte kunnat gissa ditt ord.\n")
                                end_of_game = f.return_to_main_menu()
                                return end_of_game
                    if len(word) != 5:
                        print("Du måste ange ett giltligt ord.")
                        break
                    elif word.isalpha() == False:
                        print("Ordet får inte innehålla nummer eller andra symboler.\n")  
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
            print("Filen 'hints.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")  


def check_hints(user_word, python_guess, correct_spot, correct_char, len_hints, hints):

    correct_position = 0
    correct_letter = 0
    correct_hints = 0
    wrong_hints = 0
    
    for r in range(len_hints):
        hint = hints[r]
        python_guess = hint[0]
        if user_word == python_guess:
            print("\nPython gissade faktiskt på rätt ord men du har angivit att det var fel.\nVänligen kontrollera dina dina inmatningar bättre och försök igen.\n")
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
        print(f"\nDu har angivit fel antal rätt positioner eller rätt bokstäver i {wrong_hints} av dina tips.\nVänligen kontrollera dina inmatningar bättre och försök igen.")
        print("Tryck på valfri tangent för att fortsätta.\n")
        return "wrong"
    elif correct_hints > 0:
        print(f"\nDu har angivit rätt antal rätt positioner och rätt bokstäver i {correct_hints} av dina tips.\nBra jobbat!")
        print("Tryck på valfri tangent för att fortsätta.\n")
        return "correct"
from functions_for_words import get_word

def user_guess():
    num_of_guesses = 0
    end_of_game = False
    word = get_word()
    
    while not end_of_game:
        guess = input("Gissa på ett ord: ").lower()
        num_of_guesses += 1
        if len(guess) != 5:    
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == word.lower():
            print("Du gissade rätt!")
            print(f"Du hade totalt {num_of_guesses} gissningar.")
            end_of_game = True
            return end_of_game
        else:
            correct_position = 0
            correct_letter = 0

            for i, l in enumerate(word.lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            print(f"\n{correct_position} bokstäver på RÄTT plats!\n{correct_letter} korrekta bokstäver men på FEL plats.")
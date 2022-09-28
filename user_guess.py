from functions_for_words import get_word

def user_guess():
    num_of_guesses = 0
    end_of_game = False
    word = get_word()
    guesses_words = []
    correct_position = 0
    correct_letter = 0
    
    while not end_of_game:
        
        guess = input("Guess a word: ").lower()
        num_of_guesses += 1
        
        if len(guess) != 5:    
            print("Kindly enter a valid word.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Kindly enter a valid word.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == word.lower():
            print("You guess was correct!")
            print(f"You had a total of {num_of_guesses} guesses.")
            end_of_game = True
            return end_of_game
        elif guess in guesses_words:
            print("You have already guessed the word. Please try another one.")
        elif guess == "quit":
            exit()
        else:
            guesses_words.append(guess)
            
            for i, l in enumerate(word.lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            print(f"\n{correct_position} letter on CORRECT place!\n{correct_letter} correct letter but on INCORRECT place.")
            
import game.functions as f
import game.save_load as sl
import game._highscore as h


def game_func(num_of_guesses, word, guessed_words): # Gamemode 1, player vs computer
        
    print("You can end the game by typing 'i give up' or 'quit'.")   
    print("You can save the game by typing 'save game'.")
    
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGuess a word: ").lower()
        num_of_guesses += 1
        to_many_l = 0
        
        for char in guess:
            count = guess.count(char)
            if count > 1:
                to_many_l = count
                break
        
        while num_of_guesses % 5 == 0: # To make sure the user knows how to quit the game and save the game. Good to have if the user forgets.
            print("DYou can end the game by typing 'i give up' or 'quit'.") 
            print("You can save the game by typing 'save game'.")
            break
        
        if guess == "save game":
            num_of_guesses -= 1 # The guess is not counted if the user saves the game
            sl.save_game(word, guessed_words, num_of_guesses)
        
        elif guess == "i give up" or guess == "quit":
            print(f"The word was {word}")
            f.quit_game()
        
        elif to_many_l > 1:
            print("The word contains dublicates. Kindly choose a valid word.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        
        elif len(guess) != 5:    
            print("The word has to be 5 letters. Kindly choose a valid word.")
            num_of_guesses -= 1 
        
        elif guess.isalpha() == False:
            print("The word has to be 5 letters. Kindly choose a valid word.")
            num_of_guesses -= 1 
        
        elif guess == word.lower():
            print("Your guess was correct!")
            
            if num_of_guesses == 1:
                print(f"You had a total of {num_of_guesses} guess.\n")
            else:
                print(f"You had a total of {num_of_guesses} guesses.\n")
            end_of_game = h.highscore(num_of_guesses)
        
        elif guess in guessed_words:
            print("You have already guessed for that word. Try another one.")
            num_of_guesses -= 1 
        
        else:
            guessed_words.append(guess)
            for i, l in enumerate(word.lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            print(f"\n{correct_position} letters in the CORRECT position!\n{correct_letter} CORRECT letters but in the WRONG position.")
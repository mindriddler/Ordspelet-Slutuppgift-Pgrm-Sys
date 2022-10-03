import game.functions as f
import game.save_load as sl
import game._highscore as h


def game_func_1(num_of_guesses, word, guessed_words): # Gamemode 1, player vs computer
        
    print("Du kan avsluta spelet genom att skriva 'jag ger upp'.")   
    print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
    
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1
        to_many_l = 0
        
        for char in guess:
            count = guess.count(char)
            if count > 1:
                to_many_l = count
                break
        
        while num_of_guesses % 5 == 0:
            print("Du kan avsluta spelet genom att skriva 'jag ger upp'.") # To make sure the user knows how to quit the game. Good to have if the user forgets.
            print("Du kan spara ditt spel genom att skriva 'spara spelet'.")
            break
        
            
        if guess == "spara spelet":
            num_of_guesses -= 1 # The guess is not counted if the user saves the game
            sl.save_game(word, guessed_words, num_of_guesses)
        
        elif guess == "jag ger upp":
            print(f"Ordet var {word}")
            f.quit_game()
        elif to_many_l > 1:
            print("Ditt ord innehåller dubletter. Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif len(guess) != 5:    
            print("Ditt ord måste innehålla 5 bokstäver. Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Ditt ord måste innehålla 5 bokstäver. Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == word.lower():
            print("Du gissade rätt!")
            if num_of_guesses == 1:
                print(f"Du hade totalt {num_of_guesses} gissning.\n")
            else:
                print(f"Du hade totalt {num_of_guesses} gissningar.\n")
            end_of_game = h.highscore(num_of_guesses)
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
import game.functions as f
import game.save_load as sl
import game._highscore as h
import game.word_functions as w


# Gamemode 1, player vs computer
def game_func_1(num_of_guesses, word, guessed_words, end_of_game):

    print("Du kan avsluta spelet genom att skriva 'jag ger upp'.")
    print("Du kan spara ditt spel genom att skriva 'spara spelet'.")

    while not end_of_game:
        guess = input("\nGissa på ett ord: ").lower()
        if guess == "spara spelet":
            num_of_guesses -= 1  # The guess is not counted if the user saves the game
            sl.save_game_gm1(word, guessed_words, num_of_guesses)
            continue
        elif guess == "jag ger upp" or guess == "quit":
            print(f"Ordet var {word}")
            f.quit_game()
        elif guess == word.lower():
            print("Du gissade rätt!")
            if num_of_guesses == 1:
                print(f"Du hade totalt {num_of_guesses} gissning.\n")
            else:
                print(f"Du hade totalt {num_of_guesses} gissningar.\n")
            end_of_game = h.highscore(num_of_guesses)

        validation = w.check_if_word_valid(guess, guessed_words)
        if validation == "not valid":
            continue
        else:
            num_of_guesses += 1
            while num_of_guesses % 6 == 0:  # To make sure the user knows how to quit the game and save the game. Good to have if the user forgets.
                print(
                    "Du kan avsluta spelet genom att skriva 'jag ger upp' eller 'quit'."
                )
                print(
                    "Du kan spara ditt spel genom att skriva 'spara spelet'.")
                break
            guessed_words.append(guess)
            checked = w.check_pos(guess, word)
            print(
                f"\n{checked[0]} bokstäver på RÄTT plats!\n{checked[1]} korrekta bokstäver men på FEL plats."
            )

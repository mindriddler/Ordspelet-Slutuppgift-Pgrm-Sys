import random
import game.functions as f
import game.hint_functions as h_f
import game.word_functions as w
import game.save_load as s_f


# Gamemode 2, computer vs player
def game_func_2(user_word, python_list, num_of_turns, end_of_game):

    while not end_of_game:

        try:
            num_of_turns += 1
            word = random.choice(python_list)

            if num_of_turns % 6 == 0:
                w.python_words_left(python_list)

            answer = w.right_or_wrong(user_word, word)
            if answer == "fel":
                python_list = w.checking_python_guess(python_list, word,
                                                      user_word)
            elif answer == "quit":
                f.quit_game()
            elif answer == "spara spelet":
                s_f.save_game_gm2(user_word, python_list, num_of_turns)
            elif answer == None or answer == True:
                end_of_game = True
            else:
                print("Du måste ange 'rätt' eller 'fel'.")
                continue
        except TypeError as error:
            print(error)
            end_of_game = True
        except IndexError:
            print(
                "\nPython har inte fler ord kvar att gissa på. Kontrollerar gissningar."
            )
            input("Tryck på valfri tangent för att fortsätta...")
            end_of_game = h_f.get_hints(user_word)
            return end_of_game

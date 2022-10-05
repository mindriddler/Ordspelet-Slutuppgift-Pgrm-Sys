import random
import game.functions as f
import game.hint_functions as h_f
import game.word_functions as w

def game_func_2(): # Gamemode 2, computer vs player
    
    end_of_game = False
    num_of_turns = 0
    user_word = w.player_word()
    python_list = w.create_word_list()
    
    while not end_of_game:
        
        try:
            num_of_turns += 1
            word = random.choice(python_list)
            
            
            if num_of_turns % 5 == 0:
                w.python_words_left(python_list, num_of_turns)
            
            answer = w.right_or_wrong(user_word, word)
            if answer == "fel":
                python_list = w.checking(python_list, word, user_word)
            elif answer == "quit":
                f.quit_game()
            elif answer == None or answer == True:
                end_of_game = True
            else:
                print("Du måste ange 'rätt' eller 'fel'.")
                continue
        except TypeError:
            end_of_game = True
        except IndexError:
            print("\nPython har inte fler ord kvar att gissa på. Kontrollerar gissningar.")
            input("Tryck på valfri tangent för att fortsätta...")
            end_of_game = h_f.get_hints(user_word)
            return end_of_game
            


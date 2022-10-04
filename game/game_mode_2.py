import random
import game.functions as f
import msvcrt as m
import game.hint_functions as h_f

def game_func_2(): # Gamemode 2, computer vs player
    
    end_of_game = False
    num_of_turns = 0
    user_word = f.player_word()
    python_list = f.create_word_list()
    
    while not end_of_game:
        
        try:
            num_of_turns += 1
            word = random.choice(python_list)
            answer = main_func_gamemode_2(python_list, user_word, word, num_of_turns)
            
            if answer == "wrong":
                python_list = checking(python_list, word, user_word)
            elif answer == "quit":
                f.quit_game()
            elif answer == None:
                end_of_game = True
            else:
                print("You need to type 'right' or 'wrong'.")
                continue
        except TypeError:
            end_of_game = True
        except IndexError:
            print("\nPython has no more words to guess. Checking hints.")
            print("Press any key to continue.")
            m.getch()
            end_of_game = h_f.get_hints(user_word)
            return end_of_game
            

def main_func_gamemode_2(python_list, user_word, word, num_of_turns):
    
    end_of_game = False
    
    while not end_of_game:
        if num_of_turns % 5 == 0:
            print("\nYou can end the game by typing 'quit'.")
            choice = input("Do you want to know how many potential words python has left?: ").lower()
            if choice == "yes":
                print(python_list)
                print(f"Python has {len(python_list)} words left.")
            elif choice == "quit":
                f.quit_game()
            else:
                pass

        print(f"\nYour word: {user_word}")
        print(f"Python's guess: {word}")

        answer = input("Kindly type if the guess was right or wrong: ").lower()
        if answer == "right":
            print("Python managed to make the correct guess!")
            end_of_game = f.return_to_main_menu()
        elif answer == "wrong":
            return answer
        elif answer == "quit":
            f.quit_game()
        else:
            print("You need to type 'yes' or 'no'.")
            continue


def checking(python_list, word, user_word):    
    

    while True:
        correct_spot = input("How many CORRECT characters in the CORRECT position?: ")
        correct_char = input("How many CORRECT characters in the WRONG position?: ")

        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("You need to enter numbers. Try again")
            continue
        elif correct_char == "quit" or correct_spot == "quit":
            f.quit_game()
        elif int(correct_spot) + int(correct_char) > 5:
            print("\nYou must have entered the wrong numbers. Try again.")
            continue
        else:
            
            correct_letters = int(correct_spot) + int(correct_char)
            
            if correct_letters == 0:
                python_list = [word for word in python_list if not len(set(user_word).intersection(set(word))) == 5]
            elif correct_letters >= 1:
                python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
                if word in python_list:
                    python_list.remove(word)
            h_f.save_hint(word, user_word, correct_spot, correct_char)
            return python_list
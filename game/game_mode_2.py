import random
import game.functions as f
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
            
            
            if num_of_turns % 5 == 0:
                python_words_left(python_list, num_of_turns)
            
            answer = right_or_wrong(user_word, word)
            if answer == "fel":
                python_list = f.checking(python_list, word, user_word)
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
            

def python_words_left(python_list, num_of_turns):
    
    if num_of_turns % 5 == 0:
        print("\nDu kan avsluta spelet genom att skriva 'quit'.")
        choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower()
        if choice == "ja":
            print("") # New line. Visste inte hur jag kunde få den att fungera när jag anväder en * i nästa print.
            print(*python_list, sep=', ')
            print(f"Python har {len(python_list)} ord kvar att gissa på.")
        elif choice == "quit":
            f.quit_game()
        else:
            pass


def right_or_wrong(user_word, word):
    end_of_game = False
        
    while not end_of_game:
        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")

        answer = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if answer == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif answer == "fel":
            return answer
        elif answer == "quit":
            f.quit_game()
        else:
            print("Du måste ange 'rätt' eller 'fel'.")
            continue
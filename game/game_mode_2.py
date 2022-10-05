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
            answer = main_func_gamemode_2(python_list, user_word, word, num_of_turns)
            
            if answer == "fel":
                python_list = f.checking(python_list, word, user_word)
            elif answer == "quit":
                f.quit_game()
            elif answer == None:
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
            

def main_func_gamemode_2(python_list, user_word, word, num_of_turns):
    
    end_of_game = False
    
    while not end_of_game:
        if num_of_turns % 5 == 0:
            print("\nDu kan avsluta spelet genom att skriva 'quit'.")
            choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower()
            if choice == "ja":
                print(python_list)
                print(f"Python har {len(python_list)} kvar att gissa på.")
            elif choice == "quit":
                f.quit_game()
            else:
                pass

        print(f"\nDitt ord: {user_word}")
        print(f"Pythons gissning: {word}")

        answer = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        if answer == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = f.return_to_main_menu()
        elif answer == "fel":
            return answer
        elif answer == "quit":
            f.quit_game()
        else:
            print("Du måste ange 'rätt' eller 'fel'.")
            continue
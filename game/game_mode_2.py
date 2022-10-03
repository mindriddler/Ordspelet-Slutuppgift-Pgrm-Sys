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
            
            if answer == "fel":
                python_list = checking(python_list, word, user_word)
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
            print("Tryck på valfri tangent för att fortsätta.")
            m.getch()
            end_of_game = f.get_hints()
            end_of_game = True
            

def main_func_gamemode_2(python_list, user_word, word, num_of_turns):
    
    end_of_game = False
    
    while not end_of_game:
        
        try:
            if num_of_turns % 5 == 0:
                print("\nDu kan avsluta spelet genom att skriva 'quit'")
                choice = input("Vill du veta hur många potentionela ord python har kvar?: ").lower() # Utökning av programmet som PDF filen föreslagit
                if choice == "ja":
                    print(python_list)
                    print(f"Python har {len(python_list)} kvar att gissa på.")
                elif choice == "quit":
                    f.quit_game()
                else:
                    pass
        except IndexError:
            print("\nPython har inte fler ord kvar att gissa på.\nKontrollerar gissningar.\n")
            
            
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
        
        
def checking(python_list, word, user_word):    
    
    
    while True:
        correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
        correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
        
        
        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("Du måste skriva in siffror. Försök igen.")
            continue
        elif correct_char == "quit" or correct_spot == "quit":
            f.quit_game()
        else:
            pass
        
        correct_letters = int(correct_spot) + int(correct_char)
        
        if correct_letters == 0:
            python_list = [word for word in python_list if not len(set(user_word).intersection(set(word))) == 5]
        elif correct_letters >= 1:
            python_list = [word for word in python_list if len(set(user_word).intersection(set(word))) >= correct_letters]
            if word in python_list:
                python_list.remove(word)
        h_f.save_hint(word, user_word, correct_spot, correct_char)
        return python_list
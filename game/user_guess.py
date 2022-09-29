from functions import highscore, get_word
import menu

def user_guess():
    num_of_guesses = 0
    end_of_game = False
    word = "polis" #get_word()
    guessed_words = []
        
    print("Du kan avsluta spelet genom att skriva 'quit'")
        
    while not end_of_game:
        correct_position = 0
        correct_letter = 0
        guess = input("\nGissa på ett ord: ").lower()
        num_of_guesses += 1


        if len(guess) != 5:    
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess.isalpha() == False:
            print("Vänligen ange ett giltligt ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == word.lower():
            print("Du gissade rätt!")
            if num_of_guesses == 1:
                print(f"Du hade totalt {num_of_guesses} gissning.\n")
            else:
                print(f"Du hade totalt {num_of_guesses} gissningar.\n")
            choice = input("Vill du skriva in dig på toplistan?: ").lower()
            if choice == "ja":
                name = input("Vänligen ange ditt fulla namn: ").title()
                end_of_game = True
                highscore(name, num_of_guesses)
            elif choice == "nej":
                play_again = input("Vill du återvända till huvudmenyn?: ").lower()
                if play_again == "ja":
                    end_of_game = True
                    menu.main_menu()
                elif play_again == "nej":
                    print(f"Avslutar spelet.\nHa en bra dag!")
                    end_of_game = True
                else:
                    print("Du måste ange 'ja' eller 'nej'.")
        elif guess in guessed_words:
            print("Du har redan gissat på det ordet. Prova med ett annat ord.")
            num_of_guesses -= 1 # To not count the guess if it's not valid
        elif guess == "quit":
            exit()
        else:
            guessed_words.append(guess)
            for i, l in enumerate(word.lower()):
                if l == guess[i]:
                    correct_position += 1
                elif l in guess:
                    correct_letter += 1
            print(f"\n{correct_position} bokstäver på RÄTT plats!\n{correct_letter} korrekta bokstäver men på FEL plats.")


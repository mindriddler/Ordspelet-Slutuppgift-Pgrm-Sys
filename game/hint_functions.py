import json
import msvcrt as m
import game.functions as f


def save_hint(word, user_word, correct_spot, correct_char):        
    
    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as f:
            hint_list = json.load(f)
    except FileNotFoundError:
    # If the file doesn't exist, use default values
        hint_list = []
        
    hint_list.append((word, user_word, correct_spot, correct_char))
    with open('data\hints.txt', 'w', encoding="utf-8") as f:
        json.dump(hint_list, f)
        
        
def get_hints():
    word_list = f.create_word_list()
    to_many_l = 0
    hint_no = 0
    word = input("\nVad var ditt ord? ").lower()
    
    
        
    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as file:
            hints = json.load(file)
            len_hints = len(hints)
                    
            for r in range(len_hints):
                        
                hint = hints[r]
                hint_no = r + 1
                python_guess = hint[0]
                user_word = hint[1]
                correct_spot = int(hint[2])
                correct_char = int(hint[3])

                for char in word:
                    count = word.count(char)
                    if count > 1:
                        to_many_l = count
                            
                if word == "visa mitt ord":
                    print(f"Ordet var '{user_word}'.")
                    print("Tryck på valfri tangent för att fortsätta kontrollen.\n")
                    m.getch()
                elif to_many_l > 1:
                    print("Ditt ord innehåller dubletter.\nOch det är därför python inte kunnat gissa ditt ord.\n")
                    end_of_game = True
                    return end_of_game
                elif len(word) != 5:
                    print("Du måste ange ett giltligt ord.")
                    break
                elif word.isalpha() == False:
                    print("Ordet får inte innehålla nummer eller andra symboler.\n")
                elif word != user_word:
                    print("Ordet du angav stämmer inte överens med det ordet du angav när du startade spelet.")
                    print("Om du har glömt bort ditt ord, skriv: 'visa mitt ord'.")
                    print("Tryck på valfri tangent för att fortsätta.")
                    m.getch()
                    break
                else:
                    check_hints(user_word, python_guess, correct_spot, correct_char, hint_no)
            if word not in word_list:
                end_of_game = f.add_word_to_words(word)
                return end_of_game
    except FileNotFoundError:
        print("Filen 'hints.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")             



def check_hints(user_word, python_guess, correct_spot, correct_char, hint_no):
    if user_word == python_guess:
        print("Python gissade på rätt ord men du angav att det var fel ord!\nVänligen ha bättre översikt nästa gång.")
        print("Tryck på valfri tangent för att återvända till huvudmenyn")
        m.getch()
        end_of_game = True
        return end_of_game
    
    correct_position = 0
    correct_letter = 0
    
    for i, l in enumerate(user_word.lower()):
        if l == python_guess[i]:
            correct_position += 1
        elif l in python_guess:
            correct_letter += 1    
        
    if correct_position != correct_spot or correct_letter != correct_char:
        print(f"\nPython har gissat på ordet: '{python_guess}'.\nDitt ord var '{user_word}'.")
        print(f"På gissning {hint_no} har du har svarat att det var {correct_spot} rätt bokstäver på rätt plats och {correct_char} rätt bokstäver på fel plats.")
        print(f"När det egentligen är {correct_position} rätt bokstäver på rätt plats och {correct_letter} rätt bokstäver på fel plats.")
        print("Du har alltså svarat fel på ditt svar.")
        print("Tryck på valfri tangent för att återgå till huvudmenyn.")
        correct_position = 0
        correct_letter = 0
        m.getch()
    else:
        if correct_position == correct_spot and correct_letter == correct_char:
            print(f"\nPython har gissat på ordet: '{python_guess}'.\nDitt ord var '{user_word}'.")
            print(f"På gissning {hint_no} har du har svarat att det var {correct_position} rätt bokstäver på rätt plats och {correct_letter} rätt bokstäver på fel plats.")
            print("Du har alltså svarat rätt på ditt svar. Bra jobbat!\n")
            correct_position = 0
            correct_letter = 0
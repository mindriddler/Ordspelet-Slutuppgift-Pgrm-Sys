import os



def return_to_main_menu():
    while True:
        go_back = input("Vill du återvända till huvudmenyn?: ").lower()
        if go_back == "ja":
            end_of_game = True
            return end_of_game
        elif go_back == "nej":
            quit_game()
        else:
            print("Du måste ange 'ja' eller 'nej'.")
            continue


def remove_hints():
    if os.path.exists('data\hints.txt'):
        os.remove('data\hints.txt')


def quit_game():
    print("Avslutar spelet.\nHa en bra dag!")
    remove_hints()
    exit()


def player_word():    
    
    while True:
        user_word = input("Vad är ditt ord?: ").lower()
        to_many_l = 0
        
        for char in user_word:
            count = user_word.count(char)
            if count > 1:
                to_many_l = count
                break
        
        if to_many_l > 1:
            print("Ditt ord innehåller dubletter. Vänligen ange ett giltligt ord.\n")
        elif len(user_word) != 5:
            print("Du måste ange ett giltligt ord.")
        elif user_word.isalpha() == False:
            print("Ordet får inte innehålla nummer eller andra symboler.\n")
        else:
            print("Du kan avsluta spelet genom att skriva 'quit'")
            return user_word


def create_word_list():
    try:
        with open("data\words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print("Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen.")
        exit()


def add_word_to_words(word):
    
    print("""\nDu verkar inte ha gjort några fel med dina ledtrådar.
Därför har jag kommit fram till att ditt ord saknas i ordlistan
och kommer därför lägga till det för framtida spel.
Tack för ditt bidrag!\n""")
    try:
        with open('data\words.txt', 'a+', encoding="utf-8") as f:
            f.write("\n" + word)
    except FileNotFoundError:
        print("Kunde inte hitta ordlistan. Kan inte lägga till ordet.")
        return FileNotFoundError
    

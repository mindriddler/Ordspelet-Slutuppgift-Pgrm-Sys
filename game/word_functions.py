import random
import game.functions as f
import game.hint_functions as h_f


def get_word():
    try:
        file = open("data\words.txt", "r", encoding="utf-8")
        words = file.read()
        listOfWords = words.split("\n")
        randWord = random.choice(listOfWords)
        return randWord
    except FileNotFoundError:
        print(
            "Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen."
        )
        exit()


def player_word():

    while True:
        user_word = input("Vad är ditt ord?: ").lower()

        validation = check_if_word_valid(user_word, guessed_words=[])
        if validation == "not valid":
            continue
        else:
            print("Du kan avsluta spelet genom att skriva 'quit'.")
            print("Du kan spara spelet genom att skriva 'spara spelet'.")
            return user_word


def create_word_list():
    try:
        with open("data\words.txt", "r", encoding="utf-8") as words:
            word_lst = [word.strip() for word in words.readlines()]
        return word_lst
    except FileNotFoundError:
        print(
            "Filen 'words.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen."
        )
        exit()


def add_word_to_words(word):

    print("""Du verkar inte ha gjort några fel med dina ledtrådar.
Därför har jag kommit fram till att ditt ord saknas i ordlistan
och kommer därför lägga till det för framtida spel.
Tack för ditt bidrag!\n""")
    try:
        with open('data\words.txt', 'a+', encoding="utf-8") as file:
            file.write("\n" + word)
            print("Ordet har lagts till i ordlistan.")
            input("Tryck på valfri tangent för att fortsätta.")
            f.clear_screen()
            end_of_game = True
            return end_of_game
    except FileNotFoundError:
        print("Kunde inte hitta ordlistan. Kan inte lägga till ordet.")
        return FileNotFoundError


def check_pos(guess, word):

    while True:
        correct_position = 0
        correct_letter = 0

        for i, l in enumerate(word.lower()):
            if l == guess[i]:
                correct_position += 1
            elif l in guess:
                correct_letter += 1
        return correct_position, correct_letter


def correlation(correct_spot, correct_char, python_list, word, user_word):

    correct_letters = int(correct_spot) + int(correct_char)

    if correct_letters == 0:
        python_list = [
            word for word in python_list
            if not len(set(user_word).intersection(set(word))) == 5
        ]
        if word in python_list:
            python_list.remove(word)
    elif correct_letters >= 1:
        python_list = [
            word for word in python_list
            if len(set(user_word).intersection(set(word))) >= correct_letters
        ]
        if word in python_list:
            python_list.remove(word)
    return python_list


def check_if_word_valid(guess, guessed_words):

    to_many_l = 0

    for char in guess:
        count = guess.count(char)
        if count > 1:
            to_many_l = count
            break

    if to_many_l > 1 or len(guess) != 5 or guess.isalpha() == False:
        print(
            "Ditt ord är inte ett giltligt ord. Kontrollera och välj ett nytt."
        )
        return "not valid"
    elif guess in guessed_words:
        print("Du har redan gissat på det ordet. Prova med ett annat ord.")
        return "not valid"
    else:
        return "valid"


def checking_python_guess(python_list, word, user_word):

    while True:
        correct_spot = input("Hur många RÄTT bokstäver på RÄTT plats?: ")
        correct_char = input("Hur många RÄTT bokstäver på FEL plats?: ")
        if correct_spot.isdigit() == False or correct_char.isdigit() == False:
            print("Du måste skriva in siffror. Försök igen.")
            continue
        elif correct_char == "quit" or correct_spot == "quit":
            f.quit_game()
        elif int(correct_spot) + int(correct_char) > 5:
            print("\nDu måste ha angivit fel siffror. Försök igen.")
            continue
        else:
            h_f.save_hint(word, user_word, correct_spot, correct_char)
            return correlation(correct_spot, correct_char, python_list, word,
                               user_word)


def python_words_left(python_list):

    print("\nDu kan avsluta spelet genom att skriva 'quit'.")
    choice = input(
        "Vill du veta hur många potentionela ord python har kvar?: ").lower()
    if choice == "ja":
        print(
            ""
        )  # New line. Visste inte hur jag kunde få den att fungera när jag anvnäder en * i nästa print.
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

        answer = input(
            "Vänligen ange om gissningen är rätt eller fel: ").lower()
        if answer == "rätt":
            print("Python lyckades gissa rätt!")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif answer == "fel" or answer == "spara spelet" or answer == "quit":
            return answer
        else:
            print("Du måste ange 'rätt' eller 'fel'.")
            continue
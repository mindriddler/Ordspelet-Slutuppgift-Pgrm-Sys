import json
import game.functions as f
import game.word_functions as w


def save_hint(word, user_word, correct_spot, correct_char):

    try:
        with open('data\hints.txt', 'r', encoding="utf-8") as file:
            hint_list = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, use default values
        hint_list = []

    hint_list.append((word, user_word, correct_spot, correct_char))
    with open('data\hints.txt', 'w', encoding="utf-8") as f:
        json.dump(hint_list, f)


def get_hints(user_word):

    word_list = w.create_word_list()
    end_of_game = False

    while True:
        word = input("\nVad var ditt ord?: ").lower()
        if word == "visa mitt ord":
            print(f"Ordet var '{user_word}'.")
            input("Tryck på valfri tangent för att fortsätta kontrollen...")
        elif user_word != word:
            print(
                "Ordet du angav stämmer inte överens med det ordet du angav när du startade spelet.\nOm du har glömt bort ditt ord, skriv: 'visa mitt ord'."
            )
        else:
            validation = w.check_if_word_valid(word, guessed_words=[])
            if validation == "valid":
                break
            else:
                continue

    while not end_of_game:
        try:
            with open('data\hints.txt', 'r', encoding="utf-8") as file:
                hints = json.load(file)

                corr_or_wrong = check_hints(word, hints)

                if corr_or_wrong == "wrong":
                    end_of_game = f.return_to_main_menu()
                    return end_of_game
                elif corr_or_wrong == "correct":
                    if word not in word_list:
                        end_of_game = w.add_word_to_words(word)
                        return end_of_game
                else:
                    return end_of_game
        except FileNotFoundError:
            print(
                "Filen 'hints.txt' måste finnas i data mappen för att spelet ska fungera.\nVänligen lägg till filen och försök igen."
            )


def check_hints(word, hints):

    correct_hints = 0
    wrong_hints = 0
    len_hints = len(hints)

    for r in range(len_hints):
        hint = hints[r]
        guess = hint[0]
        user_word = hint[1]
        correct_spot = int(hint[2])
        correct_char = int(hint[3])
        if word == guess:
            print(
                "\nPython gissade faktiskt på rätt ord men du har angivit att det var fel.\nVänligen kontrollera dina inmatningar bättre och försök igen.\n"
            )
            end_of_game = f.return_to_main_menu()
            return end_of_game
        else:
            pos = w.check_pos(word, guess)

            if pos[0] != correct_spot or pos[1] != correct_char:
                wrong_hints += 1
            elif pos[0] == correct_spot and pos[1] == correct_char:
                correct_hints += 1

    if wrong_hints > 0:
        print(
            f"\nDu har angivit fel antal rätt positioner eller rätt bokstäver i {wrong_hints} av dina tips.\nDärför har Python inte kunnat gissa ditt ord.\nVänligen kontrollera dina inmatningar bättre och försök igen."
        )
        input("Tryck på valfri tangent för att fortsätta.\n")
        return "wrong"
    elif correct_hints > 0:
        print(
            f"\nDu har angivit rätt antal rätt positioner och rätt bokstäver i dina tips.\nBra jobbat!"
        )
        input("Tryck på valfri tangent för att fortsätta.\n")
        return "correct"
import json
from operator import itemgetter
import game.functions as f
from itertools import islice
import os


def highscore(num_of_guesses):

    while True:
        choice = input(
            "Vill du spara ditt resultat i highscore listan?: ").lower()
        if choice == "ja":
            name = input("Vänligen ange ditt fulla namn: ").title()
            try:
                with open('data\highscore.txt', 'r') as file:
                    highscores = json.load(file)
            except FileNotFoundError:
                # If the file doesn't exist, use default values
                highscores = []

            highscores.append((name, num_of_guesses))
            highscores = sorted(highscores, key=itemgetter(1),
                                reverse=False)[:10]
            with open('data\highscore.txt', 'w') as file:
                json.dump(highscores, file)

            highscores = []
            print("Din poäng har sparats!")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif choice == "nej":
            print("Din poäng har inte sparats.")
            end_of_game = f.return_to_main_menu()
            return end_of_game
        elif choice == "quit":
            f.quit_game()
        else:
            print("Du måste ange 'ja' eller 'nej'.")
            continue


def print_highscore():

    try:
        with open('data\highscore.txt', 'r') as file:
            highscores = json.load(file)
            limit = 10
        print("\nNuvarande topp 10 bästa spelrundor!")
        print("-----------------------------------")
        for item in islice(highscores, limit):
            print(f"{item[0]}: {item[1]} gissningar")
        print("-----------------------------------")
    except FileNotFoundError:
        print(
            "Det finns ingen sparad poäng än. Spela spelet för att spara din poäng."
        )
        input("\nTryck på valfri tangent för att återvända till huvudmenyn.")

    try:
        average_guesses = sum([item[1]
                               for item in highscores]) / len(highscores)
        print(
            f"\nMedelvärdet på antal gissningar är: {average_guesses} stycken."
        )
        input("\nTryck på valfri tangent för att återvända till huvudmenyn.")
    except UnboundLocalError:
        pass


def reset_highscore():
    reset_done = False

    while not reset_done:
        password = input("Ange lösenord: ").lower()
        if password == "qwerty123":
            additional_check = input(
                "Är du säker på att du vill återställa highscoren?: ").lower()
            if additional_check == "ja":
                if os.path.exists('data\highscore.txt'):
                    os.remove('data\highscore.txt')
                    print(
                        "Highscore har nollställts!\nÅtergår till huvucmenyn.")
                    reset_done = True
                else:
                    print(
                        "Det finns förnärvarande inget highscore sparat. Kan inte återställa.\nÅtergår till huvudmenyn."
                    )
                    reset_done = True
            elif additional_check == "nej":
                print("Återgår till huvudmenyn.")
                reset_done = True
            elif additional_check == "quit":
                f.quit_game()
            else:
                print("Du måste ange 'ja' eller 'nej'.")
                continue
        elif password == "huvudmeny":
            print("Återgår till huvudmenyn.")
            reset_done = True
        elif password == "quit":
            f.quit_game()
        else:
            print(
                "Fel lösenord. Försök igen eller återgå till huvudmenyn genom att skriva 'huvudmeny'."
            )
            continue
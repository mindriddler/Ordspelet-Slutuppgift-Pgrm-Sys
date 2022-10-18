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
    try:
        if os.path.exists('data\hints.txt'):
            os.remove('data\hints.txt')
    except PermissionError:
        pass


def quit_game():
    print("Avslutar spelet.\nHa en bra dag!")
    # remove_hints()
    exit()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
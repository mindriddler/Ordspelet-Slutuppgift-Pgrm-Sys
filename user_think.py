import random
from functions_for_words import create_word_list

num_of_guesses = 0
end_of_game = False

game_list = create_word_list()



def user_think():
    
    global end_of_game
    global game_list
    
    user_word = "Polis".lower()
    
    while not end_of_game:
        word = random.choice(game_list)
        print(len(game_list))
        print(f"Ditt ord: {user_word}")
        print(f"Pythons gissning: '{word}'")
        player_check = input("Vänligen ange om gissningen är rätt eller fel: ").lower()
        
        if player_check == "rätt":
            print("Grattis, du vann!")
            end_of_game = True
        elif player_check == "fel":
            correct_spot = input("Hur många rätt bokstäver på rätt plats?: ")
            correct_char = input("Hur många rätt bokstäver på fel plats?: ")
            total_right_chars = int(correct_spot) + int(correct_char)
        
            
        if total_right_chars == 0:
            game_list = [word for word in game_list if not len(
                (set(user_word)).intersection(set(word))) == 5]
        elif total_right_chars >= 1:
            game_list = [word for word in game_list if len(
                set(user_word).intersection(set(word))) >= total_right_chars]
            if word in game_list:
                game_list.remove(word)
        print(len(game_list))









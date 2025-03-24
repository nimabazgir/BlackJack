import os
import random
import black_jack_art

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_replace(sample_list,check_item,replace_item):
    for i, word in enumerate(sample_list):
        if word == check_item:
            sample_list[i] = replace_item

def deal_card():
    """It Retruns a Random Card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if len(cards)==2 and sum(cards)==21:
        return 0
    if 11 in cards and sum(cards)>21:
        # list_replace(cards,11,1)
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,pc_score):
    if user_score == pc_score:
        return "Draw 😼"
    elif pc_score == 0:
        return "Lose, The opponent has BlackJack 🙀"
    elif user_score == 0:
        return "Win with a BlackJack 😻"
    elif user_score > 21:
        return "You went over, you lose 😿"
    elif pc_score > 21:
        return "Opponent went over. You Win 😸"
    elif user_score > pc_score:
        return "You Win 😺"
    else:
        return "You Lose 😾"

def start_game():
    user_cards = []
    pc_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    while not game_over:

        clear_screen()
        print(black_jack_art.logo)

        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"    Your cards: {user_cards}, Current Score: {user_score}")
        print(f"    Computer's First Card: {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal_again == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
        
        while pc_score != 0 and pc_score < 17:
            pc_cards.append(deal_card())
            pc_score = calculate_score(pc_cards)
        
        print(f"    Your final hand: {user_cards}, final Score: {user_score}")
        print(f"    Computer's final hand: {pc_cards}, final Score: {pc_score}")
        print(compare(user_score,pc_score))
        
        # print(f"[debug] user cards: {user_cards}")        
        # print(f"[debug] pc cards: {pc_cards}")
        # print(f"[debug] game over: {game_over}")
while input("Do You want to play a Game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    start_game()
    
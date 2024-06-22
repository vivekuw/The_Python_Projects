# 4
import random
from logo import logo
print(logo)
def deal_card():
    """return the random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# 6
def calculate_score(cards):
    """take a list of cards and return the score calculated from the cards"""
    # 7
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # 8
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# 13
def compare(user_score, computer_score):
    if user_score ==computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Computer has a blackjack."
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. you lose"
    elif computer_score > 21:
        return "opponent went over. You Win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"

def blackjack():
    # 5
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 11
    while not is_game_over:
        # 9
        user_scorce = calculate_score(user_cards)
        computer_scorce = calculate_score(computer_cards)
        print(f"   Your Cards {user_cards} ,current scores {user_scorce}")
        print(f"   Computer Cards {user_cards[0]} ")

        if user_scorce == 0 or computer_scorce == 0 or user_scorce > 21 or computer_scorce > 21:
            is_game_over = True
        else:
            # 10
            user_should_deal = input("type 'y' to get another card , type 'no' to pass :- ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            elif user_should_deal == 'n':
                is_game_over = True

    # 12
    while computer_scorce != 0 and computer_scorce < 17:
        computer_cards.append(deal_card())
        computer_scorce = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} , final score: {user_scorce}")
    print(f"Computer final hand: {computer_cards} , final score: {computer_scorce}")
    print(compare(user_scorce, computer_scorce))

# 14
continue_game = input("!!!!!!!!!Do you want to play blackjack? type 'y' or 'n' :- ").lower()
if continue_game == 'y':
    blackjack()
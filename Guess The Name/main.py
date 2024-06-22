from logo import logo

import random
computer_guess = random.randint(0, 100)

print(logo)
print("Welcome the Guess Number Game")
print("I am thinking number between 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
def check_guess(user, computer):
    if user > computer:
        print("     Too high.")
    elif user < computer:
        print("     Too low.")
    elif user == computer:
        print("     You Win.")

if difficulty == 'easy':
    chances = 10
    while chances != 0:
        print(f"You {chances} chances left.")
        user = int(input("Make a guess"))
        check_guess(user, computer_guess)
        chances -= 1
        if user == computer_guess:
            break

elif difficulty == 'hard':
    chances = 5
    while chances != 0:
        print(f"You {chances} chances left.")
        user = int(input("Make a guess: "))
        check_guess(user, computer_guess)
        chances -= 1
        if user == computer_guess:
            break

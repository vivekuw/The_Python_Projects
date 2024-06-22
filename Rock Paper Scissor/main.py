import random
from logo import paper, rock, scissor
print("Welcome the Rock, Paper, Scissor Game")
your_name = input("Your Name :- ").capitalize()
round_play = int(input("How many round you want to play? :-"))
random_count = 0
choice_count = 0
draw_count = 0
random = random.randint(0, 2)
i = 0
while i != round_play:
    choice = int(input("What do you choose? Type 0 - Rock, 1 - Paper, 2 - scissor:- "))
    if choice == 0:
        i += 1
        print(rock)
        print(" \nVS ")
        if random == 2:
            choice_count += 1
            print(scissor)
            print("You Win !!!!!")
        elif random == 0:
            draw_count += 1
            print(rock)
            print("You Draw !!!!!")
        elif random == 1:
            random_count += 1
            print(paper)
            print("You Lost !!!!!")
    elif choice == 1:
        i += 1
        print(paper)
        print(" \nVS ")
        if random == 2:
            random_count += 1
            print(scissor)
            print("You Lost !!!!!")
        elif random == 0:
            choice_count += 1
            print(rock)
            print("You Win !!!!!")
        elif random == 1:
            draw_count += 1
            print(paper)
            print("You Draw !!!!!")
    elif choice == 2:
        i += 1
        print(scissor)
        print(" \nVS ")
        if random == 2:
            draw_count += 1
            print(scissor)
            print("You Draw !!!!!")
        elif random == 0:
            random_count += 1
            print(rock)
            print("You Lost !!!!!")
        elif random == 1:
            choice_count += 1
            print(paper)
            print("You Win !!!!!")
    else:
        print("You type the wrong number")

print("\nThe Point Table")
print(f"The Total Round is {round_play}")
print(f"{your_name} your id {choice_count} \nComputer is {random_count} \nDraw is {draw_count}")

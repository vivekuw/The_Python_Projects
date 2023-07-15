import random
list=["rock","paper","scissor"]
computer_choice=random.choice(list)
a='y'
print("A GAME OF ROCK, PAPER & SCISSOR")
while a.lower()=='y':
    print("ENTER YOUR CHOICE ")
    user_input=input("TYPE HERE:")
    print(f"You choose the {user_input} and the computer choose {computer_choice}")

    if user_input.lower() ==computer_choice:
        print("the is game is tie")
    elif user_input.lower() == "rock":
        if computer_choice=="scissor":
            print("you win the game")
        elif computer_choice=="paper":
            print("you loose")
    elif user_input.lower()=="paper":
        if computer_choice=="rock":
            print("you win the game")
        elif computer_choice=="scissor":
            print("you loose")
    elif user_input.lower()=="scissor":
        if computer_choice=="paper":
            print("you win the game")
        elif computer_choice=="rock":
            print("you loose")
    a=input("Do you what to play again\n y for yes and n for no:")
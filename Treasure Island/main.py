from logo import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("enter you want to go left or right? type. ").lower()
if first == "left":
    second = input("you want to Wait or swin ? type. ").lower()
    if second == "wait":
        third = input("which door you want to open red or blue or yellow ?  type. ").lower()
        if third == "yellow":
            print("     You Win!!!!!!!!!!!!   ")
        elif third == "red":
            print('''Burned by fire.
                            Game Over.''')
        elif third == "blue":
            print('''Eaten by beasts.
                            Game Over.''')
        else:
            print("Game Over.")
    else:
        print('''Attacked by trout.
                        Game Over''')
else:
    print('''Fall into a hole.
                    Game Over. ''')

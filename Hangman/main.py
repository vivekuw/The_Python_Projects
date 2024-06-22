import random
from stage import stages, logo
from words import word_list
print(logo)
# random choice
chosen_word = random.choice(word_list)

# display the blank
display = []
lenght_chosen_word: int = len(chosen_word)
for i in range(lenght_chosen_word):
    display += "_"

# lives
lives = 6

#  main
end_of_game = False
while not end_of_game:
    # Guess the letter from User
    guess_letter = input("guess a letter: ").lower()

    if guess_letter in display:
        print(f"you already there is {guess_letter}")
    # display the correct guess letter
    for position in range(lenght_chosen_word):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter


    if guess_letter not in chosen_word:
        lives -= 1
        print(f"you guess {guess_letter}, that not in the word. you lose live")
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])

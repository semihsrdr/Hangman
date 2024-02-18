import random
import stages,words

print(stages.stages[0])

word_list=words.words

chosen_word=random.choice(word_list)

print("Welcome to the hangman...")
print("You have 7 lives for the guessing")
print()
number_of_lives=6


display=[]
for i in chosen_word:
    display.append("-")
for index in display:
    print(index, end=" ")
print()
while True:
    if chosen_word==''.join(display):
        print("You won")
        break

    while True:
        player_guess = input("Enter your guess letter (only letter please): ")
        if len(player_guess)==1:
            player_guess = player_guess.lower()
            break

    if player_guess not in chosen_word:
        number_of_lives-=1
    if player_guess in display:
        print("You have already entered this letter!")

    for position in range(len(chosen_word)):
        if chosen_word[position]==player_guess:
            display[position]=player_guess

    for index in display:
        print(index,end=" ")
    if number_of_lives==0:
        print("Word is :",chosen_word)
        print("Game Over!!!")
        break
    print(stages.stages[number_of_lives])

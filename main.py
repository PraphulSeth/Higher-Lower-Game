from art import *
from game_data import data
import random
import os 

def clear():
    os.system('cls')

print(logo)
# print(len(data))
score = 0
should_continue = False

person2 = list(data[random.randint(0,49)].values())

print("Compare the following personalities.")

while not should_continue:
    person1 = person2
    person2 = list(data[random.randint(0,49)].values())
    print(f"{person1[0]}, {person1[2]} from {person1[3]} {vs} {person2[0]}, {person2[2]} from {person2[3]}")
    print("Which of the above personalities have more followers?")
    which_one = input(f"For {person1[0]} type 'A'\nFor {person2[0]} type 'B'\n").lower()
    
    if which_one == 'a' and person1[1] > person2[1]:
        score += 1
        clear()
        print(f"You're Right. Your score is {score}")
    elif which_one == 'b' and person1[1] < person2[1]:
        score += 1
        clear()
        print(f"You're Right. Your score is {score}")
    else:
        print(f"You're wrong. Your score is {score}. Game Over.")
        exit()



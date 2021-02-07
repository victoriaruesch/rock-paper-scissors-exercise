# game.py

import os
import random

from dotenv import load_dotenv

load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("-------------------")
print("WELCOME TO MY APP!")
print(f"PLAYER: '{PLAYER_NAME}'")

import random

print("-------------------")
print(f"Welcome'{PLAYER_NAME}' my Rock-Paper-Scissors game...")
print("-------------------")


#
# asking user for an input 
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

#
#validate the user selection
#
# stop the program (not try to determine the winer)
#... if the user choice is invalid

user_choice = user_choice.lower()

options = ("paper", "rock" , "scissors")
if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()

#print(x)
#printing many things separated by commas
#print ("You chose:", x, "another string", "something else", x)
#print("You chose: ", x)

#string concat:
#print("You chose: " + x)

#string interpolation / format string usage
print(f"You Chose: {user_choice}")

#print("You chose: " + x)

#
# simulating a computer input
#

computer_choice = random.choice (options)

print(f"The Computer Chose: {computer_choice}")


#
#determining who won
#

# when doing comparables, you have to do two equal signs

print("-------------------")

if computer_choice == user_choice: 
    print ("It's a Tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print ("Yay! You Won!")    
elif user_choice == "rock" and computer_choice == "scissors":
    print("Yay! You Won!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Yay! You Won!")  
elif user_choice == "paper" and computer_choice == "scissors":
    print ("Boo! You Lost!")
elif user_choice == "rock" and computer_choice == "paper":
    print ("Boo! You Lost!")
elif user_choice == "scissors" and computer_choice == "rock":
    print ("Boo! You Lost!")

print("-------------------")
print("Thanks for playing. Please play again!")
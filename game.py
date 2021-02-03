# game.py

import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#
# asking user for an input 
#


user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

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


options = ("paper", "rock" , "scissors")
computer_choice = random.choice(options)

print(f"The Computer Chose: {computer_choice}")













exit()

print("-------------------")

print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")
#A game application that compares two search term average monthly searches. The user has to guess which term has a higher or lower monthly search
#Import all useful libraries
import os
from data import data
import random

#Start screen
print("Welcome to the Higher or Lower game!")

#Eligibility Process  
name = input("What is your name? ")
try:
  age = int(input("Hello {}, what is your age? ".format(name.capitalize())))
except ValueError:
    print("Please input integer only...")  

if age < 8:
    print("Sorry {}, you have to be over the age of 8 to be able to play this game!".format(name))
    exit()

#Create function to clear console
def clear():
    os.system('clear')

#Create the game code
def game():
    #Initial game score
    score = 0
    first_term = random.choice(data)

    game_over = False
    while game_over == False:
        #Term comparism
        print(f'Current score: {score}\n')
        print('Which search term has more monthly searches?')

        #Selecting the terms
        first_term = random.choice(data)
        second_term = random.choice(data)

        if first_term == second_term:
            second_term = random.choice(data)
        else:
            print(f"A) {first_term['name']}, a {first_term['description']}, from {first_term['country']}")
            print(f"B) {second_term['name']}, a {second_term['description']}, from {second_term['country']}")

        #User guess
        guess = input('Is it "A" or "B"? ').upper()
        clear()

        #Get the term searchs
        A = first_term["search_count"]
        B = second_term["search_count"]

        #Compare search amounts
        if guess == 'A' and A > B:
            print(f'Correct, {first_term["name"]} has more monthly searches.')
            score += 1
        elif guess == 'A' and B > A:
            print(f'Wrong, {second_term["name"]} has more monthly searches.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        elif guess == 'B' and A < B:
            print(f'Correct, {second_term["name"]} has more monthly searches.')
            score += 1
        elif guess == 'B' and A > B:
            print(f'Wrong, {first_term["name"]} has more monthly searches.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        else:
            print('Invalid guess. Restarting the game...')
            score = 0
    
    if game_over == True:
        replay = input("Would you like to play again? Y or N")
        if replay.upper() == 'Y':
            game()
        else:
            print("Goodbye!")
            exit()
game()

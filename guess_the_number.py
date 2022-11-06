import random

#randomly generate number
#user needs to guess the number
#int input whats your guess
#if user wrong, if guess is higher than number, if guess is lower than number
#if user right, print correct

start = 1
stop = 10
number = random.randint(start, stop)

def guess_the_number():
    guess = int(input("Guess a number from 1 to 10. What's your guess? "))
    if guess != number:
        if guess > number:
            print("Your guess is too big")
        elif guess < number:
            print("Your guess is too small")
        else:
            print("Invalid answer")#break only used for loops while loop
        another_guess = input("Would you like to take another guess? Y or N? ")
        while another_guess == "Y":
            return guess_the_number() #loop back to the start
        print("Thanks for playing")
    else:
        print("Correct! The answer is", guess)

guess_the_number()

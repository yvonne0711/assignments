import random

#randomly choose a number between 1 and 6 number of sides
#print number of sides
#ask if i want to roll again yes or no
#set min of 1 and max of 6
#function that randomly gets a number between 1 and 6 and prints it

#generate random number 
#if random number within min and max, print
#else, generate again
#print the number

def dice_roll():
    min = 1
    max = 6
    no_of_sides = random.randint(min, max)
    roll_gen = input("Do you want to roll the die? Y or N? ")
    if roll_gen == 'Y':
        print("You rolled a", no_of_sides)
        roll2 = input("Do you want to roll again? Y or N? ")
        while roll2 == 'Y':
            print("You rolled a", no_of_sides)
            return dice_roll() #loop through and go back to roll_gen
        print("Thanks for playing")
    else:
        print("Thanks for playing")


dice_roll()


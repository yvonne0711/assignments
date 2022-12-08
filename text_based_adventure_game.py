# the program will let users move through rooms based on user input and get descriptions
# of each room. To create this, you’ll need to establish the direction in which the user can move, a
# way to track how far the user has moved (and therefore which room he/she is in), and to print
# out a description. You’ll also need to set limits for how far the user can move. In other words,
# create “walls” around the rooms that tell the user, “You can’t move further in this direction.”

#play or not
#define start
#define each room
#define end

#def rooms

#https://jamboard.google.com/d/16rUnUmBPtZC_0_CRwpK2of4lOusuBoAgxtu1LY5JX7Y/viewer?f=0

def room1():
    print("Welcome to room 1. Where would you like to go from here? Pick: up, left or right?")
    direction = input()
    options = ["up", "left", "right"]
    if direction == 'up':
        print("Good job, it's unlocked! You are about to enter room 3.")
        room3()
    elif direction == 'left':
        print("*Rattling noises*")
        lose()
    elif direction == 'right':
        print("Good job, it's unlocked! You are about to enter room 2.")
        room2()
    else:
        print("Invalid answer. Please try again")
        room1()

#room1()

def room2():
    print("Welcome to room 2. Where would you like to go from here? Pick: up, down or right?")
    direction = input()
    options = ["up", "down", "right"]
    if direction == 'up':
        print("Good job, it's unlocked!")
        win()
    elif direction == 'right':
        print("*Eerie noises*")
        lose()
    elif direction == 'down':
        print("Good job, it's unlocked! But you are about to enter room 1 again..")
        room1()
    else:
        print("Invalid answer. Please try again")
        room2()

#room2()

def room3():
    print("Welcome to room 3. Where would you like to go from here? Pick: up, left or right?")
    direction = input()
    options = ["up", "left", "right"]
    if direction == 'up':
        print("Good job, it's unlocked!")
        win()
    elif direction == 'right':
        print("*Creeking noises* You are about to enter room 2.")
        room2()
    elif direction == 'left':
        print("Uh oh. It's locked.")
        lose()
    else:
        print("Invalid answer. Please try again")
        room3()

#room3()

def lose():
    print("You just lost...")
    play()

#lose()

def win():
    print("Congrats! You won the game!")
    play()

#win()

#at the end
def play():
    play_input = input("Would you like to play again? Y or N? ")
    if play_input == "Y":
        start()
    elif play_input == "N":
        print("Thanks for playing! See you again.")
    else:
        print("Invalid answer.")
        play()

#play()

def start():
    username = input("Welcome to Adventure X. Please enter your name: ")
    print("Hello", username, "let's begin.")
    room1()

start()




#author hharwani
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#global variables
num_range=100
num_guesses=7
typeOfGame=False
secret_number=0

# helper function to start and restart the game
def start_game():
    global num_range
    global num_guesses
    global secret_number
    if not typeOfGame:
        num_range=100
        num_guesses=cal_numberofGuesses(100)
        secret_number=random.randrange(0,100,1)
    else:
        num_range=1000
        num_guesses=cal_numberofGuesses(1000)
        secret_number=random.randrange(0,1000,1)
    print "New game. Range is from 0 to ",num_range
    print "Number of remaining guesses is",num_guesses

'''this function calculates the appropriate number of guesses
for a given range.'''    
def cal_numberofGuesses(high):
    return math.ceil(math.log(high,2))

#this function starts a new game    
def new_game():
    start_game()
    
#helper function in case the game is lost    
def lost_game():
    print "You lost,you didnt follow binary search"
    print "Give it one more try."
    new_game()
    
# define event handlers for control panel
def range100():
    global typeOfGame
    typeOfGame=False
    start_game()
    
def range1000():
    global typeOfGame
    typeOfGame=True
    start_game()
    
'''this function compares the user's guess with the secret number 
and returns output as per instructions'''   
def input_guess(input):
    global num_guesses
    num_guesses-=1
    guess=float(input)
    print "Guess was ",guess
    print "Number of remaining guesses is",num_guesses
    if guess<secret_number:
        print "Higher!"
    elif guess>secret_number:
        print "Lower!"
    elif guess==secret_number:
        print "Correct!"
        new_game()
    if num_guesses==0:
        lost_game()

#create frame
frame=simplegui.create_frame("Guess the Number!",400,400)

#create two button for restarting the game in the desired range
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)

#create an input text to record the user's guess
frame.add_input("Enter a guess",input_guess,200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

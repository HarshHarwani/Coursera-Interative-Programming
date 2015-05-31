# Rock-paper-scissors-lizard-Spock template

import random
# helper functions
#this function returns the index of the player in the circle.
def name_to_number(name):
    index=0
    nameLower=name.lower()
    if nameLower not in ['rock','spock','paper','lizard','scissors']:
        print 'selected choice is outside the rules of the game'
        return None
    if nameLower=='rock':
        index=0
    elif nameLower=='spock':
        index=1
    elif nameLower=='paper':
        index=2
    elif nameLower=='lizard':
        index=3
    else:
        index=4
    return index

#this function returns the choice given the position in the circle.
def number_to_name(number):
    name=''
    if number not in range(5):
        print 'number not generated in the range'
        return None
    elif number==0:
        name='rock'
    elif number==1:
        name='Spock'
    elif number==2:
        name='paper'
    elif number==3:
        name='lizard'
    else:
        name='scissors'
    return name
    
#this is actually the logic, it calculates the difference of 
#index of player choices and accordingly prints who wins.
def rpsls(player_choice):
    
    #entering a new line between consecutive games.
    print ""
    
    #logic to handle variation in cases of string entered by the user.
    player_choice=player_choice.lower()
    if player_choice=='spock':
        print "Player chooses"+" "+'Spock'
    else:
        print "Player chooses"+" "+player_choice
    
    #getting the player_index using name_to_number function
    player_index=name_to_number(player_choice)
    
    #getting the computer_index using random.randrange function
    computer_index=random.randrange(0, 5, 1)
    
    #getting the computer_choice using number_to_name function
    computer_choice=number_to_name(computer_index)
    print "Computer chooses"+" "+computer_choice
    
    #calculating the difference of player and computer index.
    diff=(player_index-computer_index)%5
    if diff==0:
        print "Player and computer tie!"
    elif diff==1 or diff==2:
        print "Player wins!"
    elif diff==3 or diff==4:
        print "Computer wins!"
    else:
        print "Something went wrong"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric



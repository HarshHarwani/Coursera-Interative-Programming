# implementation of card game - Memory
import simplegui
import random
WIDTH=800
HEIGHT=100
deck=[]
pos=[]
recpos=[]
exposed=[]
state=0
turns=0
index2=0
index1=0
openCardCount=0
color="Green"
bor_color="White"
# helper function to initialize globals
def new_game():
    global deck,pos,recpos,turns,openCardCount
    turns=0
    openCardCount=0
    # two lists with numbers from 0 to 8
    deck1=[]
    deck2=[]
    for i in range(8):
        deck1.append(i)
        deck2.append(i)

    #shuffling both the lists and then combining them together
    deck=deck1+deck2
    random.shuffle(deck)

    #setting the cordinates of the numbers to be shown when the card is flipped
    x=15
    for i in range(len(deck)):
        pos.append((x,50))
        exposed.append(False)
        x+=50

    #setting the cordinates of the cards to be shown
    x_disp=0
    for i in range(len(deck)):
        recpos.append([(x_disp,0),(x_disp,100),(x_disp+50,100),(x_disp+50,0)])
        exposed[i]=False
        x_disp+=50

# define event handlers
def mouseclick(pos):
    global deck,recpos,exposed,state,turns,index2,index1,openCardCount
    index=pos[0]//50
    if exposed[index]==False:
        if state==0:
            index1=index
        exposed[index]=True
        if state==0:
            state=1
        elif state==1:
            state=2
            turns+=1
            openCardCount+=2
            index2=index
        elif state==2:
            state=1
            if deck[index1]!=deck[index2]:
                exposed[index1]=False
                exposed[index2]=False
                openCardCount-=2
            else:
                exposed[index1]=True
                exposed[index2]=True
            index1=index
            index2=0

# cards are logically 50x100 pixels in size
def draw(canvas):
    global deck,recpos,turns,WIDTH,HEIGHT,openCardCount
    label.set_text("Turns = "+str(turns))
    if openCardCount!=16:
        for i in range(len(deck)):
            if exposed[i]:
                canvas.draw_text(str(deck[i]), pos[i], 25, 'White')
            else:
                canvas.draw_polygon(recpos[i],2,bor_color,color)
    else:
        canvas.draw_text("Winner", [WIDTH/3+20,HEIGHT/2], 60, 'Red')
        canvas.draw_text("Press restart to play again", [WIDTH/3-20,HEIGHT/2+30], 25, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

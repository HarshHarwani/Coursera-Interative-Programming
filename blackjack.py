# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
current=""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self,canvas, x,y,faceDown):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [x + CARD_CENTER[0], y + CARD_CENTER[1]], CARD_SIZE)
        if faceDown==True:
            card_loc=(CARD_BACK_CENTER[0],CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_SIZE, [x + CARD_BACK_CENTER[0], y + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hand=[] # create Hand object
        self.val=0

    def get_ace_count(self):
        count=0
        for i in range(len(self.hand)):
            c=self.hand[i]
            rank=c.get_rank()
            if(rank=="A"):
                count+=1
        return count

    def __str__(self):	# return a string representation of a hand
        datastring="Hand Contains "
        for i in range(len(self.hand)):
            c=self.hand[i]
            datastring+=c.get_suit()+c.get_rank()+" "
        return datastring

    def add_card(self, card):
        self.hand.append(card) # add a card object to a hand

    def hit(self,deck):
        self.add_card(deck.deal_card())

    def get_value(self):
        self.val=0
        count=self.get_ace_count()
        for i in range(len(self.hand)):
            c=self.hand[i]
            rank=c.get_rank()
            val_card=VALUES[rank]
            self.val+=val_card
            if count==1 and self.val+10<21:
                self.val+=10
        return self.val

    def is_burst(self):
        val=self.get_value()
        if val>21:
            return True

    def draw(self, canvas, y):
        for card in self.hand:
            card.draw(canvas,100+80*self.hand.index(card),y,False)
        pass	# draw a hand on the canvas, use the draw method for cards

# define deck class
class Deck:
    def __init__(self):
        self.deck=[] # create a Deck object
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                c=Card(SUITS[i],RANKS[j])
                self.deck.append(c)

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        i=random.randrange(len(self.deck))
        return self.deck.pop(i)

    def __str__(self):
        datastring="Deck Contains "
        for i in range(len(self.deck)):
            c=self.deck[i]
            datastring+=c.get_suit()+c.get_rank()+" "
        return datastring	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player,dealer,score,current
    #if player keeeps hitting deal
    if in_play:
        score-=1
    #making the deck and shiffling it
    deck=Deck()
    deck.shuffle()
    #making dealer and player's hand
    current="Hit or Stand?"
    in_play = True
    player=Hand()
    dealer=Hand()
    player.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    dealer.hit(deck)

def hit():
    global player,dealer,current,outcome,in_play,score,deck
    if in_play==True:
        player.hit(deck)
        if player.is_burst():
                outcome="You busted,Dealer wins"
                current="Deal Again?"
                score-=1
                in_play=False
        if player.get_value()==21:
                outcome="BLACK-JACK!"
                current="New Deal?"
                score+=1
                in_play=False
    # if busted, assign a message to outcome, update in_play and score

def stand():
    global in_play,score,outcome,current
    if in_play==True:
        while dealer.get_value()<17:e
            dealer.hit(deck)
            if dealer.is_burst():
                outcome="Dealer Busted,You win"
                score+=1
        if not dealer.is_burst() and dealer.get_value()>player.get_value():
            outcome="Dealer Won."
            score-=1
        elif not dealer.is_burst() and dealer.get_value()<player.get_value():
            outcome="You Won."
            score+=1
        elif not dealer.is_burst() and dealer.get_value()==player.get_value():
            outcome="Its a tie,But Dealer Wins Ties :-("
            score-=1
    in_play=False
    current="New Deal?"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    global in_play
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Black-Jack', (75, 100), 35, 'Cyan')
    canvas.draw_text('Score:', (375, 100), 35, 'Black')
    canvas.draw_text(str(score), (475, 100), 35, 'Black')
    canvas.draw_text('Dealer', (50, 180), 25, 'Black')
    canvas.draw_text(outcome, (220, 180), 25, 'Black')
    canvas.draw_text('Player', (50, 380), 25, 'Black')
    canvas.draw_text(current, (220, 380), 25, 'Black')
    dealer.draw(canvas, 200)
    player.draw(canvas, 400)
    card = Card("S", "A")
    if in_play:
        card.draw(canvas, 100, 200, faceDown = True)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

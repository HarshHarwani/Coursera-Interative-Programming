#implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=0
paddle_vel_change=4
padd1_top=0
padd2_top=0
score1_pos = [40,40]
score2_pos = [540,40]
score1=0
score2=0
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[1,1]
LEFT = True
RIGHT = True
left_direction=False
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction:
        ball_vel[0]=-1*random.randrange(2, 4)
        ball_vel[1]=-1*random.randrange(1, 3)
    else:
        ball_vel[0]=random.randrange(2, 4)
        ball_vel[1]=-1*random.randrange(1,3)

def update_paddles():
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel,paddle_vel_change
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos +=paddle_vel_change
    elif paddle1_pos > (HEIGHT-HALF_PAD_HEIGHT):
        paddle1_pos -=paddle_vel_change
    else:
        paddle1_pos += paddle1_vel
    if paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos +=paddle_vel_change
    elif paddle2_pos > (HEIGHT-HALF_PAD_HEIGHT):
        paddle2_pos -=paddle_vel_change
    else:
        paddle2_pos += paddle2_vel
        
def update_ball():
    global ball_vel,ball_pos
    collision_top_wall=False
    collision_down_wall=False
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if ball_pos[1]<=BALL_RADIUS:
        collision_top_wall=True
    if ball_pos[1]>=(HEIGHT-1)-BALL_RADIUS:
        collision_down_wall=True
    if collision_top_wall or collision_down_wall:
        ball_vel[1]=-1*ball_vel[1]
       
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,direction  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(left_direction)
    

def draw(canvas):
    global direction,score1, score2, paddle1_pos,ball_pos,paddle2_pos, ball_pos, ball_vel,padd1_top,padd2_top,padd1_bottom,padd2_bottom
 
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    update_paddles()
    padd1_top=paddle1_pos-HALF_PAD_HEIGHT
    padd1_bottom=paddle1_pos+HALF_PAD_HEIGHT
    padd2_top=paddle2_pos-HALF_PAD_HEIGHT
    padd2_bottom=paddle2_pos+HALF_PAD_HEIGHT
    canvas.draw_line([HALF_PAD_WIDTH,padd1_top],[HALF_PAD_WIDTH,padd1_bottom], PAD_WIDTH, "Yellow")
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH,padd2_top],[WIDTH-HALF_PAD_WIDTH,padd2_bottom], PAD_WIDTH, "Yellow")
     
   
    # update ball
    update_ball()
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red","Red")
    coll_left=ball_pos[0]<=BALL_RADIUS+PAD_WIDTH
    coll_right=ball_pos[0]>=(WIDTH-1)-BALL_RADIUS-PAD_WIDTH
    onpaddle1 = (padd1_top <= ball_pos[1] <= padd1_bottom) and coll_left
    onpaddle2 = (padd2_top <= ball_pos[1] <= padd2_bottom) and coll_right
    onpaddle_right = onpaddle2 and coll_right
    onpaddle_left = onpaddle1 and coll_left
    onpaddle = onpaddle_right or onpaddle_left
    if(onpaddle):
        ball_vel[0]*=-1.1
        ball_vel[1]*=1.1
    elif coll_left:
            score2+=1
            left_direction=False
            spawn_ball(left_direction)
    elif coll_right:
            score1+=1
            left_direction=True
            spawn_ball(left_direction)
    canvas.draw_text(str(score1), score1_pos, 40, "Blue")
    canvas.draw_text(str(score2), score2_pos, 40, "Blue")
    
    # update paddle's vertical position, keep paddle on the screen
 
     
  
    # draw paddle

    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=paddle_vel_change
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=paddle_vel_change
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=paddle_vel_change
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=paddle_vel_change
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()


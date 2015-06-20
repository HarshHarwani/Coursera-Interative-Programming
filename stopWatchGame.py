# template for "Stopwatch: The Game"
import simplegui
# define global variables
globalTimeCount=0
position=[50,110]
scorePosition=[160,40]
globalFormattedTime="0:00.0"
noOfAttempts=0
successfulAttempts=0
score="0/0"
isClockRunning=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

#this format function gives us the time to the tenth of a second
#so every 600 counts we consider as a minute, 
#every 10 counts as a second and evry count as tenth of a second. 
def format(t):
    A,B,C,D=0,0,0,0
    number=int(t)
    #D is always the unit digit of the counter
    #so can be easily extracted using modulo
    D=number%10
    number=number/10
    #after extracting the unit digit deciding whether to
    #further divide the number
    if number<10:
        A=0
        B=0
        C=number
    if number>=10:
        #if the number is greater than zero as it denotes number of seconds
        #we extract the %60 part and then accordingly extract B and C by using % and /
        seconds=number%60
        C=seconds%10
        seconds=seconds/10
        B=seconds%10
        #for getting the minute count we keep subrtracting 600 from the original number till
        #is greater than zero
        minuteCount=0
        while t>0:
            t=t-600
            if t>=0:
                minuteCount+=1            
        A=minuteCount    
    return str(A)+":"+str(B)+str(C)+"."+str(D)
 
def formatScore():
    global score
    score=str(successfulAttempts)+"/"+str(noOfAttempts)

# define event handlers for buttons; "Start", "Stop", "Reset"
#start function starts the timer and sets the flag that the clock is running.
def start():
    global isClockRunning
    isClockRunning=True
    timer.start()

#stops the timer,updates the score if the stopped time is a whole number,
#sets that the clock has stopped.
def stop():    
    global noOfAttempts
    global successfulAttempts
    global isClockRunning
    if isClockRunning:
        noOfAttempts+=1
        if(globalTimeCount%10==0):
            successfulAttempts+=1
        formatScore()
    isClockRunning=False
    timer.stop()
    
#stops the timer and resets all the global variables
def reset():
    global globalFormattedTime
    global globalTimeCount 
    global noOfAttempts
    global successfulAttempts
    global isClockRunning
    isClockRunning=False
    noOfAttempts=0
    successfulAttempts=0
    formatScore()
    globalTimeCount=0
    globalFormattedTime="0:00.0"
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global globalFormattedTime
    global globalTimeCount
    globalTimeCount+=1
    globalFormattedTime=format(globalTimeCount)
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(globalFormattedTime,position,42,"White")
    canvas.draw_text(score,scorePosition,24,"Green")
    canvas.draw_text("Score:",[95,40],24,"Red")
    
# create frame
frame=simplegui.create_frame("StopWatch",200,200)

# register event handlers
start = frame.add_button('Start', start,100)
stop = frame.add_button('Stop', stop,100)
reset = frame.add_button('Reset', reset,100)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

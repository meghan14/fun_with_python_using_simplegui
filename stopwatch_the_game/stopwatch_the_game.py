#"Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
time=0
width=200
height=200
position=[width/2 - 10,height/2]
size=20
attempts=0
wins=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    deci_sec=t%10
    t=t/10
    second=(t%100)
    minute= t/60
    second=second%60
    minute=minute%60
    if (second<10):
        in_str='%d:0%d.%d' % (minute,second,deci_sec)
    else :
        in_str='%d:%d.%d' % (minute,second,deci_sec)
    return in_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
     timer.start()
    
def stop():
    timer.stop()
    global attempts,wins
    if(time is not 0):
      attempts +=1
      if (time%10 is 0):
          wins +=1
    
def reset():
    global time,attempts,win
    time=0
    attempts=0
    wins=0
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time +=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),position,size,'white')
    score= '%d/%d' % (wins,attempts)
    canvas.draw_text(score,[width-(width/4),size],size,'white')
# create frame
frame=simplegui.create_frame("STOPWATCH",width,height)
timer=simplegui.create_timer(100,time_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("Reset",reset)

# start frame
frame.start()


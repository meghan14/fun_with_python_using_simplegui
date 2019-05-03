try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

width=500
height=500
ball_xposition=[]
ball_yposition=[]
radius=20
velocity_x=[]
velocity_y=[]
acc= 1
balls=6
text_pos=[width/2-6,height/2+5]
def initialize():
    for i in range(0,balls):
        velocity_x.append(random.randrange(1,5))
        velocity_y.append(random.randrange(1,5))
        ball_xposition.append(random.randrange(radius+1,width-radius))
        ball_yposition.append(random.randrange(radius+1,height-radius))
        
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        for i in range(0,balls) :
            velocity_x[i] -= acc
    elif key is simplegui.KEY_MAP['right']:
        for i in range(0,balls):
            velocity_x[i] += acc
    elif key == simplegui.KEY_MAP['up']:
       for i in range(0,balls) :
            velocity_y[i] -= acc
    elif key == simplegui.KEY_MAP['down']:
       for i in range(0,balls) :
            velocity_y[i] += acc
 
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
       for i in range(0,balls) :
            velocity_x[i] += acc
    elif key == simplegui.KEY_MAP['right']:
       for i in range(0,balls) :
            velocity_x[i] -= acc
    elif key == simplegui.KEY_MAP['up']:
       for i in range(0,balls):
            velocity_y[i] += acc
    elif key == simplegui.KEY_MAP['down']:
       for i in range(0,balls):
            velocity_y[i] -= acc   
     
def get_color(num):
    if num is 0 :
        return 'Aqua'
    elif num is 1 :
        return 'Blue'
    elif num is 2 :
        return 'Fuchsia'
    elif num is 3 :
        return 'Gray'
    elif num is 4 :
        return 'Green'
    elif num is 5 :
        return 'Lime'
    elif num is 6 :
        return 'Maroon'
    elif num is 7 :
        return 'Navy'
    elif num is 8 :
        return 'Olive'
    elif num is 9 :
        return 'Orange'
    elif num is 10 :
        return 'Purple'
    elif num is 11 :
        return 'Red'
    elif num is 12 :
        return 'Silver'
    elif num is 13 :
        return 'Teal'
    elif num is 14 :
        return 'White'
    elif num is 15 :
        return 'Yellow'

def draw(canvas):
    for i in range(0,balls):
        if(ball_xposition[i]-radius <0 or ball_xposition[i]+radius > width): 
            velocity_x[i] = -velocity_x[i]   
        if((ball_yposition[i]+radius) > height or (ball_yposition[i]-radius) < 0):
            velocity_y[i] = -velocity_y[i]
        ball_xposition[i] += velocity_x[i]
        ball_yposition[i] += velocity_y[i]
        pos=[ball_xposition[i],ball_yposition[i]]
        canvas.draw_circle(pos,radius,2,'pink',get_color(i%16))
        #canvas.draw_text(str(i),pos,radius,'Black')

def input_handler(text_input):
    global balls
    balls=int(text_input)
    initialize()
 
frame= simplegui.create_frame("Motion",width,height)
#frame.add_textbox("Enter the no. of balls",20,20)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
#frame.set_keyup_handler(keyup)
frame.add_input('Enter the no. of Balls reqd.',input_handler,50)
initialize()
frame.start()

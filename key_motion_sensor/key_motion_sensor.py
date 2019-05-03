try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width=500
height=500
ball_position=[width/2,height/2]
radius=20
velocity=[0,0]
acc= 1
text_pos=[width/2-6,height/2+5]
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
       velocity[0] -= acc
    elif key is simplegui.KEY_MAP['right']:
       velocity[0] += acc
    elif key == simplegui.KEY_MAP['up']:
       velocity[1] -= acc
    elif key == simplegui.KEY_MAP['down']:
       velocity[1] += acc
 
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
       velocity[0] += acc
    elif key == simplegui.KEY_MAP['right']:
       velocity[0] -= acc
    elif key == simplegui.KEY_MAP['up']:
       velocity[1] += acc
    elif key == simplegui.KEY_MAP['down']:
       velocity[1] -= acc        

def draw(canvas):
    ball_position[0] += velocity[0]
    ball_position[1] += velocity[1]
    canvas.draw_circle(ball_position,radius,2,'Red','Yellow')
    
    


frame= simplegui.create_frame("Motion",width,height)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
#frame.set_keyup_handler(keyup)

frame.start()

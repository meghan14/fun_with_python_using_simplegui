try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
width=500
height=500
position=[width/2,height/2]
radius=20
velocity=3
character=''
text_pos=[width/2-6,height/2+5]
def keydown(key):
    global character
    character=chr(key)
    


def draw(canvas):
    canvas.draw_circle(position,radius,2,'Red','Yellow')
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" :    
        canvas.draw_text(character,text_pos,radius+2,"Blue")
    
    


frame= simplegui.create_frame("Motion",width,height)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)


frame.start()

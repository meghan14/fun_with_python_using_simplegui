try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width= 200
height= 200
position=[width/2,height/2]
position_text=[10,height/2]
size= 5
def incr():
    global size
    size +=5

def draw(canvas):
    if size>0 and size<width/2 and size< height/2 :
        canvas.draw_circle(position,size, 5, "white")
    else :
        canvas.draw_text("CIRCLE OUT OF SCREEN!!",position_text,10,"white") 

frame=simplegui.create_frame("home",width,height)
frame.add_button("press for increment",incr)
frame.set_draw_handler(draw)


frame.start()

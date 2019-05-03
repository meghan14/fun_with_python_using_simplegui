# "Guess the number" mini-project
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui



# initialize global variables used in your code
width=200
height=200
secret_number=random.randrange(0,100)
total_attempts=7


# helper function to start and restart the game
def new_game():
    global total_attempts
    total_attempts =7
    print("\nNEW GAME STARTED..")
    print("GUESS THE NUMBER. TOTAL ATTEMPTS = 7")


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    secret_number=random.randrange(0,100)
    new_game()
    print("INPUT RANGE IS FROM 0 to 100")
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    secret_number=random.randrange(0,1000)
    new_game()
    print("INPUT RANGE IS FROM 0 to 1000")
    
    
def input_guess(guess):
    # main game logic goes here
    global total_attempts
    num= int(guess)
    total_attempts -=1
    if (not (num is secret_number)):
      if(num < secret_number):
          print("\nTotal Attempts left = ", total_attempts)
          print("Higher")
      else :
          print("\nTotal Attempts left= ", total_attempts)
          print("Lower")
      if (total_attempts == 0):
          print("Oops! You ran out of attempts. Try again!!")
          print("The no. was ", secret_number)
          range100()
    else :
      print("\nCorrect!!")
      print("Good!! U guessed in ", 7-total_attempts," attempts=")
      range100()
    
    
    
# create frame
frame=simplegui.create_frame("GUESS THE NO. - GAME", width, height)

# register event handlers for control elements
frame.add_button("Range 100",range100)
frame.add_button("Range 1000",range1000)
frame.add_input("Enter no. guessed",input_guess,50)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric

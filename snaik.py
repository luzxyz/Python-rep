#Programa basico: Juego de la culebrita
#Basic program: Snake game

# J. Andres Gutierrez -ledzky- 2019
# This is a practice exercise, i dont own the creative nor
# ideal of the project in its totallity.
# Down here is the tutorial that i followed, it's very clever
# https://www.youtube.com/watch?v=Vi0AhyUCCkE&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ
# Tested in linux mint OS, coding with visual studio code

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    
import turtle
import time
import random

delay = 0.1

# Score
score = 0
hi_score = 200

# Set up the screen
game_ = turtle.Screen()
game_.title("Snake game practice")
game_.bgcolor("#83EB95")
game_.setup(width=500,height=500)
game_.tracer(0) # turn on/off screen updates


# Snake head
head = turtle.Turtle()
head.speed(0) # Animation speed, 0 is maximum
head.shape("square")
head.shapesize(0.95,0.95,1)
head.color("white")
head.penup() # doesnt draw anything
head.goto(0,0)
head.direction="right"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.shapesize(0.95,0.95,1)
food.color("gray")
food.penup()
food.goto(0,100)

segments = [] # snake's body segments

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write("Score: 0, Hi: 0", align="center", font=("Courier", 12, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"

def move():
    y = head.ycor()
    x = head.xcor()

    if head.direction == "up":
        head.sety(y+20)

    if head.direction == "down":
        head.sety(y-20)

    if head.direction == "right":
        head.setx(x+20)

    if head.direction == "left":
        head.setx(x-20)

def restart_game():
     # Hide segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segment list
        segments.clear()


# Keyboard events
game_.listen()
game_.onkeypress(go_up,"w")
game_.onkeypress(go_up,"W")

game_.onkeypress(go_down,"s")
game_.onkeypress(go_down,"S")

game_.onkeypress(go_left,"a")
game_.onkeypress(go_left,"A")

game_.onkeypress(go_right,"d")
game_.onkeypress(go_right,"D")


#main game loop
while True:
    game_.update()

    # Check for a collision with the border
    head_xcor = head.xcor()
    head_ycor = head.ycor()
    if head_xcor<=-240 or head_xcor>=240 or head_ycor<=-240 or head_ycor>=240:
        pen.clear()
        pen.write("It seems like you're allergic to the borders", align="center", font=("Courier", 12, "normal"))
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        pen.clear()
        pen.write("Score: {}, Hi: {}".format(score, hi_score), align="center", font=("Courier", 12, "normal"))
        restart_game()


    # check for collision
    if head.distance(food) < 20:
        # move food to a random place
        x = random.randrange(-220,220,20)
        y = random.randrange(-220,220,20)
        food.goto(x,y)
        x = str(x)
        y = str(y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.shapesize(0.95,0.95,1)
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10

        if score > hi_score:
            hi_score = score

        pen.clear()
        pen.write("Score: {}, Hi: {}".format(score, hi_score), align="center", font=("Courier", 12, "normal"))

    
    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y) 

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for head collisions with body
    for segment in segments:
        if segment.distance(head) < 20:
            pen.clear()
            pen.write("You can't promote cannibalism", align="center", font=("Courier", 12, "normal"))
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            score = 0
            pen.clear()
            pen.write("Score: {}, Hi: {}".format(score, hi_score), align="center", font=("Courier", 12, "normal"))
            restart_game()

    time.sleep(delay)

game_.mainloop()
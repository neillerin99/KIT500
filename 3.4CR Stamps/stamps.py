"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "NEIL EDRIANE LERIN"

from turtle import Turtle
import random 

def place_stamp(stamper: Turtle, x: float, y: float, ink: str):
    """
    Draws the author's initials with the bottom-left corner of the drawing at (x, y)
    """
    old_ink: str
    old_direction: float
    old_x: float 
    old_y: float
    
    old_ink = stamper.pencolor()
    old_direction = stamper.heading()
    old_x = stamper.pos()[0]
    old_y = stamper.pos()[1]
    
    stamper.pencolor(ink)
    # Code block to move the starting position to the left, to center the initials upon writing
    stamper.penup()
    stamper.goto(x + 50,y)
    stamper.pendown()
    
    # code block to draw the initial N
    stamper.left(90) 
    stamper.forward(150) 
    stamper.right(150) 
    stamper.forward(170) 
    stamper.left(150) 
    stamper.forward(150) 

    # code block to create a space between letters and reposition the header
    stamper.penup()
    stamper.right(90)
    stamper.forward(20)
    stamper.right(90)
    stamper.pendown()

    # code block to draw the Initial L
    stamper.forward(150)
    stamper.left(90)
    stamper.forward(90)
    stamper.penup()
    stamper.pencolor(old_ink)
    stamper.goto(old_x, old_y)
    stamper.setheading(old_direction)

def main():
    t = Turtle() # The turtle graphics object

    place_stamp(t, -500 ,-200, 'blue')
    place_stamp(t, 100 , 300, 'red')
    # place_stamp(t)
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    # t.speed(5)

    # You will call your function (eventually several times) here
    # For example, place_stamp(t) during Stage 1 of the task

    # Avoid closing the window automatically
    t.screen.mainloop()


if __name__ == "__main__":
    main()

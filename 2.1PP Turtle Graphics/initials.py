"""
KIT101 2.1PP Turtle Graphics

This program draws my initials (NL) using turtle graphics.
"""

__author__ = "NEIL EDRIANE LERIN"

import turtle as t


def main():
    t.speed(3)
    t.color('red')  # set pointer color to red

    # Code block to move the starting position to the left, to center the initials upon writing
    t.penup()
    t.left(180)
    t.forward(100)
    t.pendown()
    
    # code block to draw the initial N
    t.right(90) 
    t.forward(150) 
    t.right(150) 
    t.forward(170) 
    t.left(150) 
    t.forward(150) 

    # code block to create a space between letters and reposition the header
    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.pendown()

    # code block to draw the Initial L
    t.forward(150)
    t.left(90)
    t.forward(90)

    t.hideturtle() # hide the turtle head
    t.mainloop()  # Avoid closing the window automatically


if __name__ == "__main__":
    main()

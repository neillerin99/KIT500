"""
Demonstration of importing modules and combining their abilities.

Note that we could have just imported turtle and used turtle. as a prefix for
turtle commands or even used from turtle import * to make all turtle functions
available without the need for a prefix.
"""

__author__ = "James Montgomery"

import turtle as t
import random as r
def main():
    size:int = r.randint(10,100)
 
    # hide turtles arrow head
    t.hideturtle()
    t.forward(size)
    # Left is TURNING the pen 90 degress not moving it by 90 pixels
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    # keeps the turtle window open
    t.mainloop()
    

if __name__ == "__main__":
    main()
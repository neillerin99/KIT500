"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
"""

__author__ = "NEIL EDRIANE LERIN"

import turtle as t


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    t.speed(3)

    # set initial color to red
    t.color('red')

    # Rotate pointer by full 180 and move forward to center the initials
    t.penup()
    t.left(180)
    t.forward(100)
    t.pendown()
    
    # code block to draw the initial N
    t.right(90) # recenter the pointer to point up
    t.forward(150) # move the pointer 150 forward
    t.right(150) # reposition the pointer header to right 150 degrees
    t.forward(170) # move the pointer 170 forward
    t.left(150) # reposition the pointer header to left to revert back to up pointing position
    t.forward(150) # move the pointer 150 forward

    # code block to create a space between letters and reposition the header
    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.color('blue') # set pointer color to blue
    t.pendown()

    # code block to draw the Initial L
    t.forward(150)
    t.left(90)
    t.forward(90)

    # hide the turtle head
    t.hideturtle()

    # Avoid closing the window automatically
    t.mainloop()


if __name__ == "__main__":
    main()

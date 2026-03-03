"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "NEIL EDRIANE LERIN"

import turtle as painter


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    painter.speed(1)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...
  
    # Rotate pointer by full 180 and move forward
    # to center the initials
    painter.penup()
    painter.left(180)
    painter.forward(100)
    painter.pendown()
    
    painter.right(90) # recenter the pointer to point up
    painter.forward(150) # move the pointer 150 forward
    painter.right(150) # reposition the pointer header to right 150 degrees
    painter.forward(170) # move the pointer 170 forward
    painter.left(150) # reposition the pointer header to left to revert back to up pointing position
    painter.forward(150) # move the pointer 150 forward


    # Avoid closing the window automatically
    painter.mainloop()


if __name__ == "__main__":
    main()

"""
Description of the program or module: what it is for, what it does.
"""

__author__ = "Arthur, King of the Britons"
__version__ = "25 May 1975"

import math as m


def some_function(x: int, y: int) -> float:
    """
    One-sentence description of what function does.
    Any assumptions/requirements for it to work correctly.
    """
    local_variable: int # description of the variable

    # description of what next block of statements does/achieves
    if ...:
        ...
    else:
        ...
    ...
    return m.sqrt(x * y + 1)


def main():
    print(f"Example call: {some_function(4, 2)}")


if __name__ == "__main__":
    main()
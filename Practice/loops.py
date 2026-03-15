"""
Briefly describe the program
"""

__author__ = "Neil Edriane Lerin"

import turtle as t

def main():
    # count: int = 0
    # count_for: int = 5
    # array = ['hello', 'world', 'this']
    # # while(count < 5):
    # #     print(count)
    # #     count+=1
    
    # for x in array:
    #     print(x)
    # sides: int = 4
    # for i in range(sides):
    #     print(i)
    #     t.forward(200)
    #     t.left(90)
    # t.mainloop()        
    name: str = 'Neil'
    # for i in name:
    #     print(i)
    count:int = 0 
    while(count < len(name)):
        print(name[count])
        count+=1
    
if __name__ == "__main__":
    main()

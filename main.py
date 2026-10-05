from math import *

def Task1(x, y):
    z = 2*x*y - sin(x+3*y**2)
    return z

def Task2(x):
    if x>0:
        return 2*x*sqrt(x)
    elif x==0:
        return cos(x**5) + 5
    elif x<0:
        return (x**2)/5


while True:
    try:
        user_choose = int(input('Choose a Task (1/2): '))
        if user_choose == 1:
            inpX = input('Enter value for X: ')
            inpY = input('Enter value for Y: ')
        
            if inpX.isdigit() and inpY.isdigit():
                x = int(inpX)
                y = int(inpY)
            else:
                print('Only nubers allowed!')
            print(f'Answer: {Task1(x,y)}')
        elif user_choose == 2:
            inpX = input('Enter value for X: ')
            if inpX.isdigit():
                x = int(inpX)
            else:
                print('Only numbers allowed!')
            print(f'Answer: {Task2(x)}')
    except ValueError:
        print('Only nubers allowed!')

    
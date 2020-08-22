#import tkinter
import math

# hypotenuse
# c = √ a^2 + b^2

def hypotenuse():
    a = float(input("enter a\n"))
    a = a**2
    b = float(input("enter b\n"))
    b = b**2
    c = math.sqrt(a+b)
    print(round(c,2))


hypotenuse()



# Sources:

'''

https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
https://www.geeksforgeeks.org/round-function-python/
https://stackoverflow.com/questions/8595973/truncate-to-three-decimals-in-python

'''

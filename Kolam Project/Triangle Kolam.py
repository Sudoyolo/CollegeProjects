# Importing necessary modules
import turtle
from turtle import *

# Hides the turle
turtle.hideturtle()

#Set turtle width to 2 pixels
turtle.width(2)

# Base line on the x-y plane where from where the points are plotted
yr = -200

# Plots a line between 2 points (x1p, y1p) and (x2p, y2p)
def line(x1p, y1p, x2p, y2p):
     turtle.penup()
     turtle.goto(x1p,y1p)
     turtle.pendown()
     turtle.goto(x2p,y2p)

# Encloses a set of points
def poly(x1, y1, d, i):
    x11 = -x1
    y11 = y1
    x2 = x1 + (10 * i)
    y2 = yr - 10
    x21 = -x2
    y21 = y2
    x3 = -10 * i
    y3 = y1 + (20 * d)
    x31 = -x3
    y31 = y3
    line(x1, y1, x11, y11)
    line(x11, y11, x21, y21)
    line(x21, y21, x3, y3)
    line(x3, y3, x31, y31)
    line(x31, y31, x2, y2)
    line(x2, y2, x1, y1)

# This function is called for odd number of dots, draws a triangle around a point
def triangle(x1, y1):
    turtle.color('Black')
    x11 = -x1
    y11 = y1
    xe = 0
    ye = yr - 10
    line(x1, y1, x11, y11)
    line(x11, y11, xe, ye)
    line(xe, ye, x1, y1)

# Take input from user and then generate the Kolam
def putkolam():
     turtle.bgcolor('White')
     n = numinput('Triangle Kolam','Number of points (1,2,3...)')
     l = n
     xr = (-10) * (n-1)
     x = xr
     y = yr
     for j in range(int(n)):
         turtle.penup()
         turtle.goto(x,y)
         for k in range(int(l)):
             turtle.dot(5,'Black')
             turtle.penup()
             turtle.forward(20)
         x += 10
         y += 20
         l -= 1
     d = n - 1
     i = 1
     x = -10 * int(n)
     y = yr + 10
     l = int(n/2)
     for j in range(l):
         turtle.color('Black')
         poly(x,y,d,i)
         i += 1
         d -= 2
         x += 10
         y += 20
     if (n%2 != 0):
          triangle(x,y)

def main():
     home()
     putkolam()
     tracer(1)
     return "Done!"

if __name__=='__main__':
    msg = main()
    print(msg)
    mainloop()
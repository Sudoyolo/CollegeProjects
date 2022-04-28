# Importing necessary modules
from turtle import *
from math import sqrt
import turtle

# Hides the turle
turtle.hideturtle()

#Turns
def turn_in_right():
     turtle.color('Red')
     turtle.circle(-5*sqrt(2),180)

def turn_in_left():
     turtle.color('Yellow')
     turtle.circle(5*sqrt(2),180)

def uturn_right():
     turtle.right(45)
     turtle.color('Green')
     turtle.circle(-10,180)

def uturn_left():
      turtle.left(45)
      turtle.color('Blue')
      turtle.circle(10,180)

def main():
     turtle.bgcolor('White')
     turtle.width(3)
     n = numinput('Suzhi Kolam','Number of points (2,4,6...)')
     l = n
     xr = (-10) * (n-1)
     x = xr
     y = 0
     # Draw Dots
     for j in range(int(n)):
          turtle.penup()
          turtle.goto(x,y)
          for k in range(int(l)):
               turtle.dot(5,'Black')
               turtle.penup()
               turtle.forward(20)
          x += 20
          y += 20
          l -= 2
     x = xr + 20
     y = -20
     l = n - 2
     for j in range(int(n)):
          turtle.penup()
          turtle.goto(x,y)
          for k in range(int(l)):
               turtle.dot(5,'Black')
               turtle.penup()
               turtle.forward(20)
          x += 20
          y -= 20
          l -= 2
# Draw Kolam
     turtle.color('Black')
     x = xr
     y = -10
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown()
     d = 10 * n * sqrt(2)
     turtle.left(45)
     j = int(n)
     l = int(j/2) - 1
     for i in range(l):
          turtle.forward(d)
          turn_in_right()
          turtle.color('Black')
          turtle.forward(d)
          turn_in_left()
          turtle.color('Black')
     turtle.forward(d)
     uturn_right()
     turtle.color('Black')
     turtle.right(45)
     for i in range(l):
          turtle.forward(d)
          turn_in_left()
          turtle.color('Black')
          turtle.forward(d)
          turn_in_right()
          turtle.color('Black')
     turtle.forward(d)
     uturn_left()
     turtle.color('Black')
     return "Done!"

if __name__=='__main__':
    msg = main()
    print(msg)
    mainloop()
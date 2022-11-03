#! /usr/bin/env python3

import turtle
import os

# windows setup

window = turtle.Screen()
window.title('Pong by Metta')
window.bgcolor('black')
window.setup(width=800 , height=600)
window.tracer(0)

# Score 
averageSpeed = 0.3
scoreA = 0
scoreB = 0
maxScore = 10

# Paddle A

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=7,stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-380,0)

# Paddle B 

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=7,stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(375,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = averageSpeed
ball.dy = averageSpeed


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(" Player A : 0 Player B : 0 ", align="center" , font=("Courier",24,"normal"))



# Function

def paddleA_up():
  
  paddleA.sety(paddleA.ycor()+30)

def paddleA_down():
  
  paddleA.sety(paddleA.ycor()-30)

def paddleB_up():
  
  paddleB.sety(paddleB.ycor()+30)

def paddleB_down():
  
  paddleB.sety(paddleB.ycor()-30)


# KeyBinding

window.listen()
window.onkeypress(paddleA_up, "w")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up,"Up")
window.onkeypress(paddleB_down,"Down")



# Main game loop
while True:
  window.update()

  ## Move the Ball

  ball.sety(ball.ycor() + ball.dy)
  ball.setx(ball.xcor() + ball.dx)

  ## Border checking

  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
    os.system("aplay fire-close.wav&")

  elif ball.ycor() <-290:
    ball.sety(-290)
    ball.dy *= -1
    os.system("aplay fire-close.wav&")
    

  if ball.xcor()  > 390:
    ball.goto(0,0)
    ball.dx *= -1
    scoreA += 1
    os.system("aplay bounce.wav&")
    pen.clear()
    pen.write(" Player A : {} Player B : {} ".format(scoreA, scoreB), align="center" , font=("Courier",24,"normal"))

  elif ball.xcor()  < -390:
    ball.goto(0,0)
    ball.dx *= -1
    scoreB += 1
    os.system("aplay bounce.wav&")
    pen.clear()
    pen.write(" Player A : {} Player B : {} ".format(scoreA, scoreB), align="center" , font=("Courier",24,"normal"))

  ## paddle and ball collisions 

  if ball.xcor() > 365 and (ball.ycor() < paddleB.ycor() + 60 and ball.ycor() > paddleB.ycor() - 60 ):
    ball.setx(365)
    ball.dx *= -1
    os.system("aplay one-clap.wav&")

  elif (ball.xcor() < -370 ) and (ball.ycor() < paddleA.ycor() + 60 and ball.ycor() > paddleA.ycor() - 60 ):
    ball.setx(-370)
    ball.dx *= -1
    os.system("aplay one-clap.wav&")

  ## Game Over

  if scoreA == maxScore :
    pen.clear()
    pen.goto(0,260)
    pen.write(" Player A : 0 Player B : 0 ", align="center" , font=("Courier",24,"normal"))
    ball.goto(0,0)
    pen.goto(0,0)
    pen.write("GAME OVER", align="center" , font=("Courier",48,"normal"))
    pen.goto(0,-50)
    pen.write("Player 2 wins", align="center" , font=("Courier",32,"normal"))
    
  elif scoreB == maxScore :
    pen.clear()
    pen.goto(0,260)
    pen.write(" Player A : 0 Player B : 0 ", align="center" , font=("Courier",24,"normal"))
    ball.goto(0,0)
    pen.goto(0,0)
    pen.write("GAME OVER", align="center" , font=("Courier",48,"normal"))
    pen.goto(0,-50)
    pen.write("Player 1 wins", align="center" , font=("Courier",32,"normal"))
    

    

    

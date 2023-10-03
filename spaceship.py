##################################################################
# Author: Emmanuel Adotey Acquaye
# Purpose: 
# Acknowledgement: Original code written by Emmanuel Acquaye
##################################################################

import turtle
import random
wn=turtle.Screen()
wn.addshape("spaceship.gif")
wn.addshape("meteor.gif")
wn.addshape("laser.gif")             #adds images to window's library
wn.addshape("explosion.gif")
wn.bgcolor("black")                  #sets the background to lack



space=turtle.Turtle()
space.penup()
meteor1=turtle.Turtle()
laser= turtle.Turtle()
laser.penup()


small=turtle.Turtle()
small.color("white")
small.speed(0)
small.hideturtle()                 #hides turtle object

star =turtle.Turtle()
star.color("white")
star.speed(0)
star.hideturtle()




print("Here Are The Controls:")
print("Press 'T' to draw stars")
print("Press 'R' to spawn rocket")
print("Press 'M' to spawn meteor")
print("press 'N' to move meteor")
print("")
print("'W' is to move forward, 'S' to move backwards")
def stardraw():                                                #draws stars on the black background
    for s in range(10):
        star.penup()
        star.goto(random.randrange(-400,400),random.randrange(-400,300))
        star.pendown()
        
        star.begin_fill()
        for i in range(5):
            star.forward(50)
            star.right(144)
        star.end_fill()
    for m in range(10): 
        small.penup()
        small.goto(random.randrange(-400,400),random.randrange(-200,300))
        small.pendown()
        small.begin_fill()
        small.circle(3)
        small.end_fill()
        
   

def spaceship():                                      #spawns a spaceship for the child
    space.goto(0,-200)
    laser.goto(space.pos())
    laser.shape("laser.gif")
    laser.left(90)
    
    space.shape("spaceship.gif")
    space.left(90)
   
    
    
def spacemove_forward():                              #moves spaceship forward
   space.forward(50)
   laser.goto(space.pos())

def spacemove_back():                                 #moves spaceship backwards
    space.backward(50)
    laser.goto(space.pos())
    
def meteor():                                          #spawns a meteor
    meteor1.goto(0,400)
    meteor1.shape("meteor.gif")
    meteor1.right(90)
    
def meteor_move():                                    #meteor moves towards spaceship but is shot down by a laser
    meteor1.penup()
    meteor1.forward(300)
    laser.goto(meteor1.pos())
    meteor1.shape("explosion.gif")                    #changes shape to a different image("exllosion.gif")
    laser.hideturtle()
    
    
    

    
wn.onkey(spaceship, "r")
wn.onkey(spacemove_forward,"w")
wn.onkey(spacemove_back, "s")                       #serves a listener function
wn.onkey(meteor, "m")
wn.onkey(stardraw, "t")
wn.onkey(meteor_move, "n")
wn.listen()                


  


    
    
        













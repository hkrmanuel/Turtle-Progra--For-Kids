import turtle
wn = turtle.Screen()
jake = turtle.Turtle()

def smart():
  jake.forward(100)
  jake.left(90)
  

wn.onkey(smart, 'w')
wn.listen()


  
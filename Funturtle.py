import turtle
turtle.shape("turtle")
square= turtle.clone()
square.shape("square")
square.goto(100,100)
square.pendown()
square.goto(100,200)
triangle = square.clone()
triangle.shape("triangle")
triangle.goto(100,250)
triangle.goto(0,0)
square.goto(300,300)
square.stamp()
square.goto(100,100)
triangle.goto(300,20)
triangle.stamp()
triangle.goto(0,0)
turtle.mainloop()

UP_ARROW = "Up"
LEFT_ARROW = " Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBEAR = " space"
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
def up():
    

##  DO NOT EDIT THIS AREA
import turtle
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgpic("fl101c_geometric_gems_maze.png")

# set start position and heading
CELL_SIZE = 23
obo = turtle.Turtle()
obo.penup()
obo.goto(-240 + 2.5*CELL_SIZE, 240 - 3*CELL_SIZE)
obo.pendown()
obo.pencolor("blue")
obo.pensize(4)
obo.setheading(270)

# move two cells forward
obo.forward(2*CELL_SIZE)

##  END OF RESTRICTED AREA

#############################
## INSERT YOUR SOLUTION HERE

# move two cells forward
obo.forward(2 * CELL_SIZE)

## END OF YOUR SOLUTION
#############################

##  DO NOT EDIT THIS AREA
turtle.done()
##  END OF RESTRICTED AREA

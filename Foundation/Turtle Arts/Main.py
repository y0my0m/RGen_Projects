import turtle

def draw_attractive_design():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(0)  # Maximum speed for fast drawing
    turtle.bgcolor("black")  # Set background color to black
    pen.pensize(2)  # Set pen size to 2

    # Loop for drawing the spiral pattern
    for i in range(167):  # Adjust the number of iterations for a larger spiral
        pen.color(colors[i % 6]) # Cycle through the colors
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.right(15)
        pen.forward(i)
        
    
    
    pen.hideturtle()  # Hide the turtle when the drawing is complete

draw_attractive_design()  # Call the function to start drawing

turtle.done()  # Finish the Turtle session
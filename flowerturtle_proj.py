import turtle
window = turtle.Screen()
window.bgcolor("light blue")

def draw_rhombus(rhom_turtle):
    for i in range(1,3):
        rhom_turtle.forward(50)
        rhom_turtle.left(30)
        rhom_turtle.forward(50)
        rhom_turtle.left(150)
        
def draw_line(line_turtle):
    line_turtle.right(90)
    line_turtle.forward(220)
    line_turtle.left(95)

    for i in range(1,3):
        draw_rhombus(line_turtle)
        line_turtle.right(-140)

def draw_flower():
    rhomemon = turtle.Turtle()
    rhomemon.shape("circle")
    rhomemon.color("yellow")
    rhomemon.speed(50)

    for i in range(1,18):
        draw_rhombus(rhomemon)
        rhomemon.right(22)       

    lineman = turtle.Turtle()
    lineman.shape("arrow")
    lineman.color("dark green")
    lineman.speed(50)
    draw_line(lineman)
        
draw_flower()
 
window.exitonclick()

import turtle
n=int(input("enter the number"))
def draw_flower(petals=n, radius=100):
    angle = 360 / petals
    turtle.color("black", "black") 
    for _ in range(petals):
        draw_petal(radius)
        turtle.left(angle)
    turtle.done()
def draw_petal(radius):
    for _ in range(2):
        turtle.circle(radius, 60)   
        turtle.left(120)           
draw_flower(petals=n, radius=100) 
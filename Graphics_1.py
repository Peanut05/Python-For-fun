import turtle as tu

roo = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("black")  # Screen Bg color
wn.title("Fractal Tree Pattern")
roo.left(90)  # moving the turtle 90 degrees towards left
roo.speed(30)  # setting the speed of the turtle

def draw(l):  # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:

        roo.pensize(2)  # Setting Pensize
        roo.pencolor("yellow")  # Setting Pencolor as yellow
        roo.forward(l)  # moving turtle forward by 'l'
        roo.left(30)  # moving the turtle 30 degrees towards left
        draw(3 * l / 4)  # drawing a fractal on the left of the turtle object 'roo' with 3/4th of its length
        roo.right(60)  # moving the turtle 60 degrees towards right
        draw(3 * l / 4)  # drawing a fractal on the right of the turtle object 'roo' with 3/4th of its length
        roo.left(30)  # moving the turtle 30 degrees towards left
        roo.pensize(2)
        roo.backward(l)  # returning the turtle back to its original psition

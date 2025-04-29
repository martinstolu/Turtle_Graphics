import turtle

from Hirst_picture import random_color

"""Drawing a Spiral"""
curl = turtle.Turtle()
curl.speed("fastest")
def spiral(no_of_spiral):
    degree = int(360/ no_of_spiral)
    heading = 360 / degree
    for no in range(int(heading)):
        curl.color(random_color())
        curl.circle(100)
        curl.setheading(curl.heading() + degree)



spiral(10)
screen = turtle.Screen()
screen.exitonclick()
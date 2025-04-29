import colorgram
import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.shape('turtle')
tim.speed("fastest")

appended_random_color = []
generate_random_color = colorgram.extract('hirst color painting.jpg', 100)

for i in generate_random_color:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    appended_random_color.append((r, g, b))

def random_color():
    return random.choice(appended_random_color)



def dotting(column, row, distance):
    for col in range(column):
        for rw in range(row):
            tim.color(random_color())
            tim.dot(20)
            tim.pu()
            tim.fd(distance)
            tim.pu()

        tim.backward(distance * row)
        tim.left(90)
        tim.fd(distance)
        tim.right(90)

if __name__ == "__main__":
    dotting(6, 5, 50)
    screen = turtle.Screen()
    screen.exitonclick()
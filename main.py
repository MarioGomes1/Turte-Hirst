# import colorgram
import random
import turtle as turtle_module

tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)

colors = [(233, 226, 210), (217, 218, 224), (210, 156, 103), (108, 110, 128), (139, 141, 154), (235, 214, 226), (225, 214, 110), (186, 66, 29), (221, 236, 225), (206, 145, 175), (180, 159, 38), (102, 110, 174), (22, 23, 66), (199, 15, 3), (23, 43, 23), (228, 167, 197), (219, 80, 56), (36, 38, 15), (43, 45, 110), (232, 173, 161), (156, 170, 159), (199, 11, 21), (148, 67, 82), (212, 76, 99), (84, 101, 87), (180, 181, 218), (222, 208, 19), (42, 22, 42), (69, 73, 40), (46, 74, 50)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    print(dot_count)
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()

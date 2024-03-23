# extract colors using colorgram package
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# colors_rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     # save into tuples
#     rgb = (r, g, b)
#     colors_rgb_list.append(rgb)
#
# print(colors_rgb_list)
# print("end of program")

# Hist Painting
import random
import turtle
from turtle import Turtle, Screen

color_list = [(25, 42, 64), (130, 165, 207), (233, 149, 89), (206, 135, 147), (239, 210, 83), (194, 217, 236),
              (133, 184, 161), (27, 111, 168), (174, 59, 44), (157, 32, 30), (51, 39, 42), (177, 27, 30), (140, 67, 78),
              (38, 61, 54), (238, 209, 217), (239, 164, 152), (231, 163, 167), (51, 122, 107), (221, 79, 71),
              (1, 104, 73), (23, 62, 119), (197, 100, 109), (17, 83, 107), (61, 55, 51), (196, 222, 219),
              (186, 188, 214), (110, 126, 151), (169, 204, 192), (91, 146, 137)]

painting_turtle = Turtle()
screen = Screen()
# change color mode to rgb
turtle.colormode(255)  # 255 is for rgb mode


def draw_a_spot(dot_size):
    painting_turtle.dot(dot_size, random.choice(color_list))


def move_forward(path):
    painting_turtle.forward(path)


def start_position(n, m, path, dot_size):
    painting_width = dot_size + path * n
    painting_height = dot_size + path * m
    # negate the x, y position
    start_x = -(painting_width / 2)
    start_y = -(painting_height / 2)
    return start_x, start_y


def draw_painting(n, m, path, dot_size):
    # calculate the starting position
    start_x, start_y = start_position(n, m, path, dot_size)
    next_y = start_y
    painting_turtle.penup()  # so it won't show drawing line
    # set the starting position
    painting_turtle.setposition(start_x, start_y)
    for _ in range(m):
        for _ in range(n):
            draw_a_spot(dot_size)
            move_forward(path)
            # change to new y after paint first row of dots
        next_y += path
        painting_turtle.setposition(start_x, next_y)
        painting_turtle.speed("fastest")
    # hide turtle once finish painting
    painting_turtle.hideturtle()


# Draw the painting n=10 m=10 path=50 dot_size=20
draw_painting(10, 10, 50, 20)

screen.exitonclick()

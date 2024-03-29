# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:58:58 2024

@author: Lenovo
"""


import turtle

my_turtle_cursor = turtle.Turtle()

my_turtle_screen = turtle.Screen()


def write_inside_heart():

    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-230, 15)
    my_turtle_cursor.pencolor("#FFFFFF")
    my_turtle_cursor.write("love massage", font=("Helevetica", 30, "bold"))

def draw_complete_heart():
    my_turtle_cursor.fillcolor("#FFE87C")
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.left(140)
    my_turtle_cursor.forward(294)
    draw_left_curve_of_heart()
    my_turtle_cursor.right(190)
    draw_right_curve_of_heart()
    my_turtle_cursor.forward(294)
    my_turtle_cursor.end_fill()

def draw_left_curve_of_heart():

    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)

def draw_right_curve_of_heart():

    my_turtle_cursor.speed(50)
    for i in range(450):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.forward(1.2)

my_turtle_cursor.penup()
my_turtle_cursor.goto(0, -200)
my_turtle_cursor.pendown()
my_turtle_cursor.speed(100)

draw_complete_heart()
write_inside_heart()
turtle.done()

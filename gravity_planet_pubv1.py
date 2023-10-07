# Author: Tony Rahman | trseattle@outlook.com | www.flyingsalmon.net | October 2023 | Version: 1.0.0
# Permissions: Non-commercial use only. Modifications allowed if made available to public domain with no additional restrictions.
# Attribution: Original author: Tony Rahman | trseattle@outlook.com | www.flyingsalmon.net | Edited by: <author_name><date>


import time  
import turtle 
import math 

obj = turtle.Turtle() 
obj.shapesize(1.5) 
obj.shape("square") 
obj.color("brown") 

scale = 0.01 
g_earth = 9.8 * scale 
g_moon = 1.62 * scale 
g_mars = 3.711 * scale 
g_jupi = 24.79 * scale 
g_plut = 0.62 * scale 
g_sun = 274.0 * scale 

def drop(obj, g):

    obj.width(1) 

    window = turtle.Screen()

    height = int(window.window_height() * 0.80) 

    obj.penup() 
    obj.hideturtle() 

    obj.sety(height / 2) 
    obj.setheading(-90) 

    obj.pendown() 
    v = 0 

    obj.showturtle()
    while obj.ycor() > -height / 2:

        v = v + g 
        obj.forward(v) 

        window.update()

def time_of_fall(h, g):

    t = math.sqrt(2 * h / g)

    return t

def draw_horz_line(obj, startx, starty, linewidth ):
    '''
    Draws a line starting from point startx,starty for the width specified by linewidth param
    called by: main. This is called after each drop() call because we clear the entire screen after each drop, so needs to be redrawn before next drop.
    params: obj: turtle object for the app; startx: starting x coord of line, starty: starting y coord of line; linewidth: how wide the line should be.
    '''

    obj_height = obj.shapesize()[0] * 20 
    starty = starty - obj_height      

    obj.width(20) 

    obj.penup() 
    obj.hideturtle() 
    obj.setposition(startx, starty) 
    obj.setheading(0) 
    obj.pendown() 
    obj.forward(linewidth) 

def prep_between_drops(obj, width, height):
    """
    Clears the drawing window from previous drawings and resets the turtle
    Resets the velocity 
    Called by: main
    Calls: draw_horz_line() to draw the ground surface line

    Returns: ZERO to reset the global v var to zero before next drop.

    """

    obj.clear() 
    obj.penup() 
    obj.hideturtle() 
    obj.sety(height / 2) 

    draw_horz_line(obj, -width/2, -height/2, width)

    return 0 

pause_time = 5
window = turtle.Screen()
height = int(window.window_height() * 0.80) 
print(f"Height={height} units") 
width  = window.window_width() * 0.80 

draw_horz_line(obj, -width/2, -height/2, width)

obj.penup() 
obj.hideturtle() 
obj.goto( -10, height / 2) 
obj.write("Earth | g = 9.8 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_earth) 

fall_time = round(time_of_fall(height, g_earth), 1) 
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

time.sleep(pause_time) 
v = prep_between_drops(obj, width, height) 

obj.penup() 
obj.hideturtle() 
obj.goto( -10, height / 2) 
obj.write("Moon | g = 1.62 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_moon) 

fall_time = round(time_of_fall(height, g_moon), 1) 
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

time.sleep(pause_time) 
v = prep_between_drops(obj, width, height) 

obj.penup() 
obj.hideturtle() 
obj.goto( -10, height / 2) 
obj.write("Mars | g = 3.711 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_mars) 

fall_time = round(time_of_fall(height, g_mars), 1)
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

time.sleep(pause_time) 
v = prep_between_drops(obj, width, height)

obj.penup() 
obj.hideturtle() 
obj.goto( -10, height / 2) 
obj.write("Jupiter | g = 24.79 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_jupi) 

fall_time = round(time_of_fall(height, g_jupi), 1)
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

time.sleep(pause_time) 
v = prep_between_drops(obj, width, height)

obj.penup() 
obj.hideturtle() 
obj.goto( -10, height / 2) 
obj.write("Pluto | g = 0.62 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_plut) 

fall_time = round(time_of_fall(height, g_plut), 1)
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

time.sleep(pause_time) 
v = prep_between_drops(obj, width, height)

obj.penup() 
obj.hideturtle() 
obj.goto( 0, height / 2) 
obj.write("SUN | g = 274.0 m/s^2", font=("Arial", 16, "bold")) 

drop(obj, g_sun) 

fall_time = round(time_of_fall(height, g_sun), 1)
obj.goto(0, -height/2 -10)
fall_str = f"\tTime of fall over distance: {height} meters: {fall_time} secs"
obj.penup() 
obj.write(fall_str, font=("Arial", 10, "normal"))

window.exitonclick()

###


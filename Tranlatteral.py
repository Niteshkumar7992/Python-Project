# from googletrans import Translator
# user ="i am boy"
# Translator = Translator()
# a = Translator.translate(user,src="en",dest = "")
# print(a.text)



# print("********************************************************************************************")

# import turtle 
# import colorsys
# t = turtle.turtle()
# s = turtle.Screen().bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range (360):
#     c = colorsys.hsv_to_rgb(h,1,0.8)
#     h += 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range (2):
#         t.left(30)
#         t.circle(60)


# print("********************************************************************************************")

# import turtle
# import colorsys

# t = turtle.Turtle()  # Fix the typo: turtle.turtle() -> turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')

# t.speed(0)
# n = 70
# h = 0

# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 1/n
#     t.color(c)
#     t.left(1)
#     t.forward(1)
#     for j in range(20):
#         t.left(60)  # Provide an angle to the left turn
#         t.circle(120)  # Provide a radius to the circle

# turtle.done()


# print("********************************************************************************************")


# from turtle import *
# import colorsys
# speed(0)
# bgcolor("black")
# h = 0
# for i in range(16):
#     c= colorsys.hsv_to_rgb(h,1,1,)
#     color(c)
#     h += 0.005
#     rt(90)
#     circle(150 - j *6,90)
# #     lt(90)
# #     circle(150 - j * 6)
# #     rt




# print("********************************************************************************************")



# from turtle import *
# import colorsys

# speed(0)
# bgcolor("black")

# h = 0
# n = 36  # Number of circles to draw

# for i in range(n):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     color(c)
#     h += 1/n  # Adjust the color hue increment to cycle through colors
    
#     right(90)
#     circle(150 - i * 4, 90)  # Adjust the circle radius to decrement properly
#     left(90)
#     circle(150 - i * 4, 90)
#     left(90)
#     circle(150 - i * 4, 90)
#     right(90)
#     circle(150 - i * 4, 90)

# done()


# print("********************************************************************************************")



# from turtle import *
# import colorsys

# speed(0)
# bgcolor("black")

# h = 0
# n = 36  # Number of circles to draw

# for i in range(n):
#     c = colorsys.hsv_to_rgb(h, 1, 1)
#     color(c)
#     h += 1/n  # Adjust the color hue increment to cycle through colors
    
#     right(90)
#     circle(150 - i * 4, 90)  # Adjust the circle radius to decrement properly
#     left(90)
#     circle(150 - i * 4, 90)
#     left(90)
#     circle(150 - i * 4, 90)
#     right(90)
#     circle(150 - i * 4, 90)

# done()

# print("**********************************************************************")





from turtle import *
import colorsys
speed(0)
hideturtle()
bgcolor("black")
tracer(5)
width(2)
h = 0.001 
for i in range(90):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)
    h += 0.02

    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h += 0.02
done()    

# print("***************************************************************")




# import turtle as tur
# import colorsys as cs
# tur.setup(800,900)
# tur.speed(0)
# tur.tracer(10)
# tur.width(2)
# tur.bgcolor("black")
# for i in range(25):
#     for i in range(15):
#         tur.color(cs.hsv_to_rgb(i/15,j/25,1))
#         tur.right(90)
#         tur.circle(200  -  j * 4,90)
#         tur.left(90)
#         tur.circle(200 - j *  4  ,90)
#         tur.right(180)
#         tur.circle(50,24)
# tur.hideturtle()    
# print("**********")
# tur.done()    






# import turtle as tur
# import colorsys as cs

# tur.setup(800, 900)
# tur.speed(0)
# tur.tracer(10)
# tur.width(2)
# tur.bgcolor("black")

# for j in range(25):  # Outer loop for the number of iterations
#     for i in range(15):  # Inner loop for color and drawing pattern
#         tur.color(cs.hsv_to_rgb(i/15, 1, 1))
#         tur.right(90)
#         tur.circle(200 - j * 4, 90)
#         tur.left(90)
#         tur.circle(200 - j * 4, 90)
#         tur.right(180)
#         tur.circle(50, 24)

# tur.hideturtle()
# tur.done()














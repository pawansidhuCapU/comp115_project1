import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("midnightblue")

# Create a Turtle instance
artist = turtle.Turtle()
artist.speed(0)  # Set the fastest drawing speed

# Function to draw a star
def draw_star(x, y, size):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color("white")
    artist.begin_fill()
    for _ in range(5):
        artist.forward(size)
        artist.right(144)
    artist.end_fill()

# Function to draw the moon
def draw_moon(x, y, radius):
    artist.penup()
    artist.goto(x, y - radius)
    artist.pendown()
    artist.color("lightgray")
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Function to draw a constellation
def draw_constellation(x, y, num_stars, size_range):
    for _ in range(num_stars):
        size = random.randint(size_range[0], size_range[1])
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(50, 200)
        star_x = x + distance * math.cos(angle)
        star_y = y + distance * math.sin(angle)
        draw_star(star_x, star_y, size)

# Draw stars
draw_constellation(-200, 100, 30, [2, 5])
draw_constellation(200, -100, 20, [3, 6])
draw_constellation(-300, -200, 25, [2, 4])
draw_constellation(300, 200, 15, [3, 5])

# Draw the moon
draw_moon(-100, 200, 50)

# Hide the turtle and display the drawing
artist.hideturtle()
turtle.done()

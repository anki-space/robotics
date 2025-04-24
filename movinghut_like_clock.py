import turtle
import time
import math

# Define the hut's points relative to origin
points = {
    "A": (50, 50), "B": (200, 50), "C": (125, 150), "D": (50, 100), "E": (200, 100)
}

# Define the lines connecting the points
lines = [
    ("A", "B"),  # Base
    ("A", "D"), ("B", "E"),  # Walls
    ("D", "E"),  # Roof base
    ("D", "C"), ("E", "C")  # Roof sides
]

# Function to rotate a point around the origin in anti-clockwise direction
def rotate_point(x, y, angle):
    rad = math.radians(-angle)  # Negative angle for anti-clockwise rotation
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return (x_new, y_new)

# Set up turtle screen
turtle.setup(600, 600)
turtle.bgcolor("white")
turtle.speed(0)
turtle.tracer(0, 0)

def draw_hut(rotated_points):
    turtle.clear()
    turtle.penup()
    
    for p1, p2 in lines:
        turtle.goto(rotated_points[p1])
        turtle.pendown()
        turtle.goto(rotated_points[p2])
        turtle.penup()
    
    turtle.update()

# Animate rotation for 360 degrees
for angle in range(0, 361):
    rotated_points = {key: rotate_point(x, y, angle) for key, (x, y) in points.items()}
    draw_hut(rotated_points)
    time.sleep(0.1)  # Smooth animation

turtle.done()

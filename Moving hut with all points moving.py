import matplotlib.pyplot as plt
import numpy as np

# Define the hut's points using dictionary data structre
points = {
    "A": (2, 1), "B": (5, 1), "C": (3.5, 4), "D": (2, 3), "E": (5, 3)
}

# Define the lines connecting the points
lines = [
    ("A", "B"),  # Base
    ("A", "D"), ("B", "E"),  # Walls
    ("D", "E"),  # Roof base
    ("D", "C"), ("E", "C")  # Roof sides
]

def rotate_point(x, y, angle, pivot_x=1, pivot_y=1):
    rad = np.radians(angle)
    x_shifted, y_shifted = x - pivot_x, y - pivot_y
    x_new = x_shifted * np.cos(rad) - y_shifted * np.sin(rad) + pivot_x
    y_new = x_shifted * np.sin(rad) + y_shifted * np.cos(rad) + pivot_y
    return (x_new, y_new)



# Ask user for number of angles
num_images = int(input("Enter the number of images to display: "))
angle_diff = 5
angles = [i * angle_diff for i in range(num_images)]  # Generate angles from 0 to user input
colors = ['r', 'g', 'b', 'y'] * (num_angles // 4 )  # Alternate colors with 3 different options


# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

for i, angle in enumerate(angles):
    rotated_points = {}
    for key, (x, y) in points.items():
            rotated_points[key] = rotate_point(x, y, angle)


    # Plot rotated hut using ax.plot function

    for p1, p2 in lines:
        x_values = [rotated_points[p1][0], rotated_points[p2][0]]
        y_values = [rotated_points[p1][1], rotated_points[p2][1]]
        ax.plot(x_values, y_values,f'{colors[i]}-', linewidth=1)

    ax.plot(x_values, y_values,f'{colors[i]}-',label = f'Rotation {angle}°' )


# Final plot settings
ax.set_xlim(-3, 6)
ax.set_ylim(-3, 6)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Rotated Huts at Different Angles (Rotating every point along origin)")
ax.grid()
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define the original hut points
points = {
    "A": (2, 1), "B": (5, 1), "C": (3.5, 4), "D": (2, 3), "E": (5, 3)
}

# Define the lines connecting the points
lines = [
    ("A", "B"), ("A", "D"), ("B", "E"),  # Walls
    ("D", "E"),  # Roof base
    ("D", "C"), ("E", "C")  # Roof sides
]

# Compute relative positions with respect to A
# Extract coordinates of point A
A_x, A_y = points["A"]

# Initialize an empty dictionary for relative points
relative_points = {}

# Loop through all points in the dictionary
for key, (x, y) in points.items():

    # Skip point A as it remains constant
    if key != "A":

        # Calculate relative coordinates with respect to A
        dx = x - A_x
        dy = y - A_y

        # Store the relative position
        relative_points[key] = (dx, dy)

# Function to rotate point A around the origin
def rotate_point(x, y, angle, pivot_x=0, pivot_y=0):
    rad = np.radians(angle)
    x_shifted, y_shifted = x - pivot_x, y - pivot_y
    x_new = x_shifted * np.cos(rad) - y_shifted * np.sin(rad) + pivot_x
    y_new = x_shifted * np.sin(rad) + y_shifted * np.cos(rad) + pivot_y
    return (x_new, y_new)



# Ask user for number of angles
num_images = int(input("Enter the number of images to display: "))
angle_diff = 5
angles = [i * angle_diff for i in range(num_images)]  # Generate angles
colors = ['r', 'g', 'b', 'y'] * (num_images // 4 + 1)  # Alternate colors

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

for i, angle in enumerate(angles):
    # Rotate only A
    A = rotate_point(*points["A"], angle)

    # Compute other points based on A's new position
    rotated_points = {"A": A}
    for key, (dx, dy) in relative_points.items():
        rotated_points[key] = (A[0] + dx, A[1] + dy)

    # Plot rotated hut
    for p1, p2 in lines:
        x_values = [rotated_points[p1][0], rotated_points[p2][0]]
        y_values = [rotated_points[p1][1], rotated_points[p2][1]]
        ax.plot(x_values, y_values, f'{colors[i]}-', linewidth=1)

    # Add legend once per rotation
    ax.plot([], [], f'{colors[i]}-', label=f'Rotation {angle}°')

# Final plot settings
ax.set_xlim(-2, 6)
ax.set_ylim(-2, 6)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Rotated Huts at Different Angles (Keep A as reference Point)")
ax.grid()
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()

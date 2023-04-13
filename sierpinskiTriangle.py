import matplotlib.pyplot as plt
import numpy as np
import random

# Function to calculate the median point between two points
def median_point(p1, p2):
       return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

# Function to generate Sierpinski Triangle fractal
def sierpinski_triangle(fist_p, second_p, third_p, loops, markersize=10, new = None):
       if new is None: # If new is not provided, set it to [fist_p[0] + 1, fist_p[1] + 1]
              new = [fist_p[0] + 1, fist_p[1] + 1]
       all_points = [fist_p, second_p, third_p, new] # List to store all points (vertices and new points)
       for i in range(loops):
              chosen = random.choice([fist_p, second_p, third_p]) # Choose one of the vertices randomly
              new = median_point(new, chosen) # Calculate the median point between new point and chosen vertex
              all_points.append(new) # Add the new point to the list of all points
       all_points = np.array(all_points) # Convert list of points to NumPy array for plotting
       plt.scatter(all_points[:, 0], all_points[:, 1], s=markersize, marker='.') # Scatter plot of all points with given marker size
       plt.show() # Show the plot

# Define initial vertices of the Sierpinski Triangle
fist_p = [0, 0]
second_p = [12, 0]
third_p = [6, 15]

# Call the sierpinski_triangle function with given parameters
sierpinski_triangle(fist_p, second_p, third_p, 100000, 1)

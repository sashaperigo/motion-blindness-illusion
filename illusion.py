import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Constants
NUM_DOTS = 200
DOT_SIZE = 250
OUTSIDE_RADIUS = 3
INSIDE_RADIUS = 2
COLOR_INTERVAL = 200

fig = plt.figure()
plt.axes()

# Generate point locations. These stay constant!
def get_pts(x_prime, y_prime):
  x = np.random.randint(low=0, high=10, size=NUM_DOTS)
  y = np.random.randint(low=0, high=360, size=NUM_DOTS)

  r = [(INSIDE_RADIUS + float(val)/10.0) for val in x]
  theta = [float(val) for val in y]

  for i in range(0, NUM_DOTS):
    x_prime.append(r[i] * np.cos(theta[i]))
    y_prime.append(r[i] * np.sin(theta[i]))

x, y = [], []
get_pts(x, y)
plt.scatter([0], [0], c='w', edgecolor='none')
colors = np.random.rand(NUM_DOTS)

# Change half of the colors
def change_colors(i):
  new_colors = np.random.rand(NUM_DOTS / 2)
  for i in range(0, len(new_colors)):
    colors[i] = new_colors[i]
  plt.scatter(x, y, c=colors, s=DOT_SIZE, alpha=1, edgecolor='none')

a = anim.FuncAnimation(fig, change_colors, interval=COLOR_INTERVAL)

plt.axis('scaled')
plt.axis('off')
plt.show()
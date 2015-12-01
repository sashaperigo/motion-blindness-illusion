import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Constants
NUM_DOTS = 150
DOT_SIZE = 250
OUTSIDE_RADIUS = 3
INSIDE_RADIUS = 2

COLOR_INTERVAL = 250
ROTATE_INTERVAL = 1
DEG_SHIFT = 45
DEG_PER_MS = 5

'''
Creates a modified array of colors based on the first
randomly generated array.
'''
def shift_colors(colors1):
  colors2 = []
  tmp = np.random.rand(NUM_DOTS / 2)
  for i in range(0, len(tmp)):
    colors2.append(colors1[i])
  for i in range(0, len(tmp)):
    colors2.append(tmp[i])
  return colors2

'''
Return the array of colors that corresponds to the current value
of the color flag.
'''
def choose_colors():
  global colors1, colors2, color_flag
  if color_flag:
    return colors1
  return colors2

'''
Use trigonometry to generate a series of points within the
outside and inside circle radii using our generated values of 
x, y, and r and the current values of theta.
'''
def get_points(x_prime, y_prime):
  global r, theta
  for i in range(0, NUM_DOTS):
    x_prime.append(r[i] * np.cos(np.radians(theta[i])))
    y_prime.append(r[i] * np.sin(np.radians(theta[i])))

'''
Plot points with the current colors and values of theta.
'''
def plot_points():
  global colors, points
  x_prime, y_prime = [], []
  get_points(x_prime, y_prime)

  # Remove any existing points
  if points != None:
    points.remove()
  points = plt.scatter(x_prime, y_prime, c=choose_colors(), s=DOT_SIZE, alpha=1, edgecolor='none')

'''
Plot white dot in the middle of the circle and 100 randomly 
colored dots to begin with.
'''
def init():
  plt.scatter([0], [0], c='w', edgecolor='none')
  plot_points()

'''
Function called every 250 ms which changes the set of colors to
be displayed on the screen.
'''
def change_colors(i):
  global color_flag
  color_flag = not color_flag
  plot_points()

'''
Function called every ms which shifts all of the dots on the 
screen 3 degrees to the right or the left. Points shift 45 
degrees to the left, back to the center, then 45 degrees to the left.
'''
def rotate(i):
  global theta
  # Use counter i to figure out which way plot should shift
  direction = ((i + 1) / (DEG_SHIFT / DEG_PER_MS)) % 4
  if direction == 3 or direction == 0:
    theta = [val + DEG_PER_MS for val in theta]
  else:
    theta = [val - DEG_PER_MS for val in theta]
  plot_points()

fig = plt.figure()
plt.axes()

x = np.random.randint(low=0, high=10, size=NUM_DOTS)
y = np.random.randint(low=0, high=360, size=NUM_DOTS)

r = [(INSIDE_RADIUS + float(val) / 10.0) for val in x]
theta = [float(val) for val in y]

colors1 = np.random.rand(NUM_DOTS)
colors2 = shift_colors(colors1)
color_flag = True
points = None

a = anim.FuncAnimation(fig, change_colors, init_func=init, interval=COLOR_INTERVAL)
b = anim.FuncAnimation(fig, rotate, init_func=init, interval=ROTATE_INTERVAL)

plt.axis('scaled')
plt.axis('off')
plt.show()

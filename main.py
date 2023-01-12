import matplotlib.pyplot as plt
from PIL import Image
import time
from d_star_python_robotics import *
from d_star_new import *
from manage_grid import *


start_point = (8, 1)
end_point = (154, 81)
image = "Maze01.png"
use_pyrobotics = False


def python_star(grid, start, goal):
    m = Map(grid.width, grid.height)
    ox, oy = [], []
    for x in range(grid.width):
        for y in range(grid.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if grid.getpixel((x,y)) != white:
                ox.append(x)
                oy.append(grid.height - y)
    m.set_obstacle([(i, j) for i, j in zip(ox, oy)])

    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.plot(start[0], start[1], "og")
        plt.plot(goal[0], goal[1], "xb")
        plt.axis("equal")

    dstar = Dstar(m)
    start = m.map[start[0]][start[1]]
    end = m.map[goal[0]][goal[1]]
    #print(end)
    rx, ry = dstar.run(start, end)


grid = Image.open(image)
grid = grid.convert('RGB')

m = Map(grid.width, grid.height)

if use_pyrobotics:
    # Python Robotics D* algo
    start_point_robotics = (start_point[0], grid.height - start_point[1])
    end_point_robotics = (end_point[0],  grid.height - end_point[1])

    start_time = time.time()
    python_star(grid, start_point_robotics, end_point_robotics)
    end_time = time.time()
else:
    # Self D* algo
    start_time = time.time()
    d_star(start_point, end_point, grid)
    end_time = time.time()

    plt.plot(start_point[0], start_point[1], "og")
    plt.plot(end_point[0], end_point[1], "xb")

    plt.imshow(grid)

elapsed_time = end_time - start_time
print('Time elapsed:', elapsed_time)

plt.show()
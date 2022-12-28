import matplotlib.pyplot as plt
from PIL import Image
import time

show_animation = False


from d_star_python_robotics import *
from d_star_new import *
#from d_star_set import d_star as d_set

from manage_grid import *


def python_star(grid, start, goal):
	m = Map(grid.width, grid.height)
	ox, oy = [], []
	for x in range(grid.height):
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
	print(end)
	rx, ry = dstar.run(start, end)
	#if show_animation:
		



start_point = (20, 20)
end_point = (20, 22)
image = "Maze00.png"
grid = Image.open(image)

grid = grid.convert('RGB')




m = Map(grid.height, grid.height)

start_time = time.time()
#python_star(grid, start1, goal1)
end_time = time.time()
#elapsed_time = end_time - start_time
#print('Time Robotics elapsed:', elapsed_time/60)

start_point = (start_point[0], grid.height - start_point[1])

end_point = (end_point[0],  grid.height - end_point[1])

plt.plot(start_point[0], start_point[1], "og")
plt.plot(end_point[0], end_point[1], "xb")

start_time = time.time()
d_star(start_point, end_point, grid)
end_time = time.time()

elapsed_time = end_time - start_time
print('Time elapsed:', elapsed_time/60)


plt.imshow(grid)
plt.show()


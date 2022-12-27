import matplotlib.pyplot as plt
from PIL import Image

black = (0, 0, 0)
white = (255, 255, 255)
gray = (149, 149, 149)
red = (255, 0, 0)

blue = (0, 255, 255)

def get_neighbours(grid, xy):
	x = xy[0]
	y = xy[1]
	width = grid.width
	height = grid.height
	to_return = []

	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if i == 0 and j == 0:
				continue
			if x + i < 0 or x + i >= width:
				continue
			if y + j < 0 or y + j >= height:
				continue
			new_xy = (x + i, y + j)
			to_return.append((new_xy, grid.getpixel(new_xy)))
	return to_return

def print_neighbours(grid, n):
	for point in n:
		grid.putpixel(point[0], blue)

def print_path(grid, list):
	for point in list:
		grid.putpixel(point, blue)



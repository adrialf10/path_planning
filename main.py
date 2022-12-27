import matplotlib.pyplot as plt
from PIL import Image

from d_star import *
from test import *
grid = Image.open("Maze00.png")
grid = grid.convert('RGB')

#point = (10, 10)


d_star((10,10),(10,8), grid)

#n = get_neighbours(grid, point)
pixel = grid.getpixel((11, 5))
print()
plt.imshow(grid)
plt.show()
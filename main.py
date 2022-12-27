import matplotlib.pyplot as plt
from PIL import Image
import time

#from d_star import *
from d_star_new import *

from manage_grid import *
grid = Image.open("Maze01.png")
grid = grid.convert('RGB')


start_time = time.time()
d_star((9,2),(153,80), grid)

end_time = time.time()

elapsed_time = end_time - start_time
print('Time elapsed:', elapsed_time/60)

#n = get_neighbours(grid, point)
pixel = grid.getpixel((11, 5))
plt.imshow(grid)
plt.show()




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

#img = Image.open("grid.png")
img = Image.open("Maze00.png")

imgarr = np.array(img)
print(imgarr)
"""
print(img.getpixel((19,1)))

img.putpixel((19,1), (255,0,0))

print(img.getpixel((19,1)))
"""
plt.imshow(img)
plt.show()

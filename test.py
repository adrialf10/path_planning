import matplotlib.pyplot as plt
from PIL import Image

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gm = Image.open("GridMap.png")
#gm = Image.open("Maze00.png")

gm = gm.convert('RGB')

print(gm.getpixel((320,196)))
gm.putpixel((96,117), red)

plt.imshow(gm)
plt.show()

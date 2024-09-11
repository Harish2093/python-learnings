import sys
from PIL import Image

images = []
for image in sys.argv[1:]:
    img = Image.open(image)
    print(img.size)
    img = img.resize((1200, 1200))
    images.append(img)


images[0].save('output.gif', save_all=True, append_images=images[1:], duration=500, loop=0)


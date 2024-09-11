import numpy as np
from PIL import Image

from ray import Ray
image_width = 640
image_height = 360
# size of output image in pixels; one ray per pixel

fov = 90
# degrees


data = np.zeros((image_height,image_width,3), dtype=np.uint8)

for x in range(image_width):
    for y in range(image_height):
        ray_x = ((2*x)/image_width - 1) * (image_width/image_height)
        ray_y = 1 - ((2*y) / image_height)
        ray_z = -1
        # this assumes you're always looking straight towards z
        
        direction_full = np.array([ray_x, ray_y, ray_z])
        direction = direction_full/np.linalg.norm(direction_full)
        
        ray = Ray(np.array([0., 0., 0.]), direction)

        while not ray.step():
            continue

        data[y][x] = ray.get_color()
    print(f"{x}/{image_width} complete")



new_imageA = Image.fromarray(data)

new_imageA.save("test.png")
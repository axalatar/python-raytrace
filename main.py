import numpy as np
import multiprocessing
from PIL import Image

from ray import Ray

import cProfile
import pstats
from pstats import SortKey

def main():
    image_width = 400
    image_height = 225
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



    img = Image.fromarray(data)

    img.save("test.png")

cProfile.run("main()", 'restats')
p = pstats.Stats('restats')
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

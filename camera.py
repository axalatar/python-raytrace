from scene import Scene
from typing import Tuple
import numpy as np
from ray import Ray
from PIL import Image
import cProfile
import pstats
from pstats import SortKey
import math
import multiprocessing
import time
import os

from hittables.sphere import Sphere
from hittables.plane import Plane
class Camera:
    def __init__(self, dimensions: Tuple[int, int], fov: float) -> None:
        self.dimensions: Tuple[int, int] = dimensions
        self.fov = fov

    def render(self, scene: Scene, location: np.ndarray, direction: np.ndarray, anti_aliasing: bool = False, samples_per: int = 5):

        up = np.array([0, 1, 0])
        # TODO up should not be pre set, it should be variable; use quaternions for rotation!

        right = np.cross(direction, up)

        image_plane_dist = 1 / (np.tan(self.fov / 2))
        aspect_ratio = self.dimensions[0]/self.dimensions[1]

        
        data = np.zeros((self.dimensions[1], self.dimensions[0],3), dtype=np.uint8)

        for x in range(self.dimensions[0]):
            print(f"{x}/{self.dimensions[0]}")
            for y in range(self.dimensions[1]):
                u = (((2 * x) / self.dimensions[0]) - 1) * aspect_ratio
                v = 1 - ((2 * y) / self.dimensions[1])

                

                #print(Ray(self.location, normalized).render(self.scene).get_color_or_default(np.array([0, 0, 0])))

                if not anti_aliasing:
                    direction_full = (
                        direction * image_plane_dist +
                        right * u + 
                        up * v
                    )
                    normalized = direction_full / np.sqrt(direction_full.dot(direction_full))
                    data[y][x] = Ray(location, normalized).render(scene).get_color_or_default(np.array([0, 0, 0]))
                
                else:
                    u_width = 1/self.dimensions[0]
                    v_height = 1/self.dimensions[1]
                    color = np.array([0.0, 0.0, 0.0])
                    for rand_x, rand_y in zip(np.random.rand(samples_per), np.random.rand(samples_per)):
                        u_d = ((rand_x-0.5)*u_width) + u
                        v_d = ((rand_y-0.5)*v_height) + v

                        direction_full = (
                            direction * image_plane_dist +
                            right * u_d + 
                            up * v_d
                        )
                        normalized = direction_full / np.sqrt(direction_full.dot(direction_full))
                        color += Ray(location, normalized).render(scene).get_color_or_default(np.array([0.0, 0.0, 0.0]))
                    data[y][x] = color / samples_per



        img = Image.fromarray(data)

        # img.save("aaa.png")
        return img

completed = 0

def orbit_camera(camera, scene, center, angle, radius):
    # returns a render from the camera orbited clockwise. angle is in radians
    global completed

    location = np.array([math.cos(angle - math.pi) * radius + center[0], 0, math.sin(angle) * radius + center[1]])
    direction = center - location
    direction = direction / (np.linalg.norm(direction))
    render = camera.render(scene, location, direction)
    completed += 1
    print(completed)
    return render


def main():
    a = Camera((800, 400), 90)
        
    scene = Scene(
        [
            Sphere(5, np.array([0, 0, 0])),
            Plane(np.array([0, -1, 0]), np.array([0, -1, 0]))
        ]
    )
    
    # val = multiprocessing.Value('i', 0)
    # unrendered = [(a, scene, [0, 0, 0], math.radians(i), 10) for i in range(360)]

    # pool = multiprocessing.Pool(processes=1)
    # renders = pool.starmap(orbit_camera, unrendered)
    # pool.close()
    # pool.join()

    a.render(scene, np.array([10, 0, 0]), np.array([-1, 0, 0]), True, 100).save("antialias.png")

    print("Completed!")
    # renders[0].save('temp_result.gif', save_all=True,optimize=False, append_images=renders[1:], loop=0)

# cProfile.run("main()", 'restats')
# p = pstats.Stats('restats')
# p.sort_stats(SortKey.CUMULATIVE).print_stats(10)
start = time.perf_counter()
main()
b = time.perf_counter() - start
print(time.perf_counter() - start)
print(b/45)
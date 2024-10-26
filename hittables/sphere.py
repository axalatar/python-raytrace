from hittables.hittable import Hittable, HitInformation
from ray import Ray
from typing import List
import numpy as np
import math

class Sphere(Hittable):
    def __init__(self, radius: float, location: np.ndarray) -> None:
        self.radius: float = radius
        self.square_radius: float = radius ** 2
        self.location: np.ndarray = location

    def intersection(self, ray: Ray) -> HitInformation:
        l = self.location - ray.position
        tca = np.dot(l, ray.direction)
        d2 = np.dot(l, l) - tca * tca
        if(d2 > self.square_radius): 
            return HitInformation()

        thc = math.sqrt(self.square_radius - d2)
        t0 = tca - thc
        t1 = tca + thc

        if (t0 > t1): t0, t1 = t1, t0

        if (t0 < 0):
            t0 = t1
            if (t0 < 0):
                return HitInformation()
        
        pos = ray.position + (ray.direction * t0)

        relative = pos - self.location
        normal = 255 * (((relative/np.linalg.norm(relative)) / 2) + 0.5)

        return HitInformation(t0, normal, self)
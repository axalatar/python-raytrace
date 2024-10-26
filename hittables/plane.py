from hittables.hittable import Hittable, HitInformation
from ray import Ray
from typing import List
import numpy as np
import math

class Plane(Hittable):
    def __init__(self, point: np.ndarray, normal: np.ndarray) -> None:
        self.point: np.ndarray = point
        self.normal: np.ndarray = normal

    def intersection(self, ray: Ray) -> HitInformation:
        denom = np.dot(self.normal, ray.direction)

        if denom >= 1e-6:
            p0l0 = self.point - ray.position
            t = (p0l0.dot(self.normal)) / denom

            if t >= 0:
                hit_pos = (t * ray.direction) + ray.position
                # if hit_pos[0] % 0.5 >= 0.25 and hit_pos[2] % 0.5 >= 0.25:
                    # return HitInformation(t, np.array([50, 0, 0]), self)
                
                if (hit_pos[2] % 5 > 2.5) == (hit_pos[0] % 5 > 2.5):
                    return HitInformation(t, np.array([200, 200, 200]), self)
                
                else:
                    return HitInformation(t, np.array([100, 100, 100]), self)
                
                return HitInformation(t, np.array([20, 20, 20]), self)
                
            
        return HitInformation()
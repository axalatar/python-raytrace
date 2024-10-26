from typing import List
from hittables.hittable import HitInformation
from scene import Scene
import numpy as np


class Ray:

    def __init__(self, position: np.ndarray, direction: np.ndarray):

        self.position: np.ndarray = position
        self.direction: np.ndarray = direction


    def render(self, scene: Scene) -> HitInformation:
        hits = [hittable.intersection(self) for hittable in scene.hittables]
        return HitInformation.union(hits)
from typing import List
from hittables.hittable import Hittable

class Scene:
    def __init__(self, hittables: List[Hittable]) -> None:
        self.hittables: List[Hittable] = hittables
from __future__ import annotations 
from abc import ABC, abstractmethod
#from ray import Ray
from typing import List, Optional
import math
import numpy as np

class HitInformation:
    def __init__(self, distance: float = math.inf, color: Optional[List[float]] = None, obj: Optional[Hittable] = None) -> None:
        self.distance: float = distance
        self.color: Optional[List[float]] = color
        self.obj: Optional[Hittable] = obj

    def clone(self) -> HitInformation:
        """Clones this information"""
        return HitInformation(self.distance, self.color, self.obj)

    def get_color_or_default(self, default: np.ndarray) -> np.ndarray:
        """Returns the color of the object the ray hit, or a default value if nothing"""
        return self.color if self.color is not None else default
    
    def hit(self) -> bool:
        """Returns whether the ray hit the object"""
        return self.obj is not None
    
    def union(self, other: HitInformation) -> HitInformation:
        """Combines the two informations into a single which represents the closest hit object"""
        
        if self.distance >= other.distance:
            return other.clone()
        
        return self.clone()
    
    def union(informations: List[HitInformation]):
        """Combines any number of hit informations into a single which represents the closest hit object"""

        min_dist = math.inf
        min_info = None

        for info in informations:
            if min_dist > info.distance:
                min_dist = info.distance
                min_info = info
        
        return min_info.clone() if min_info is not None else HitInformation()



class Hittable(ABC):
    @abstractmethod
    def intersection(ray: 'Ray') -> HitInformation:
        """Returns the HitInformation of the ray"""
        pass


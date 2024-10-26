# from hittables.hittable import Hittable, HitInformation
# from ray import Ray
# from typing import List
# import numpy as np
# import math

# class Box(Hittable):
#     def __init__(self, length: float, location: np.ndarray) -> None:
#         self.length: float = length
#         self.location: np.ndarray = location

#     def intersection(self, ray: Ray) -> HitInformation:
#         float tmin, tmax, tymin, tymax, tzmin, tzmax;
    
#         tmin = (bounds[r.sign[0]].x - r.orig.x) * r.invdir.x;
#         tmax = (bounds[1-r.sign[0]].x - r.orig.x) * r.invdir.x;
#         tymin = (bounds[r.sign[1]].y - r.orig.y) * r.invdir.y;
#         tymax = (bounds[1-r.sign[1]].y - r.orig.y) * r.invdir.y;
        
#         if ((tmin > tymax) || (tymin > tmax))
#             return false;

#         if (tymin > tmin)
#             tmin = tymin;
#         if (tymax < tmax)
#             tmax = tymax;
        
#         tzmin = (bounds[r.sign[2]].z - r.orig.z) * r.invdir.z;
#         tzmax = (bounds[1-r.sign[2]].z - r.orig.z) * r.invdir.z;
        
#         if ((tmin > tzmax) || (tzmin > tmax))
#             return false;

#         if (tzmin > tmin)
#             tmin = tzmin;
#         if (tzmax < tmax)
#             tmax = tzmax;

#         return true;
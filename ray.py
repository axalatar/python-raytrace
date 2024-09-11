import numpy as np

class Ray:
    step_size = 0.01
    sphere_location = [0, 0, -3]
    sphere_radius = 1
    lifetime = 300

    def __init__(self, position, direction):
        # position & direction are numpy vectors

        self.position = position
        self.direction = direction
        self.color = [0, 0, 0]
        self.steps = 0

    def step(self):
        self.position += self.direction * self.step_size
        if ((self.sphere_radius ** 2) >= sum((self.position - self.sphere_location) ** 2)):
            
            direction_from_sphere = self.position - np.array(self.sphere_location)
            normal = direction_from_sphere / (np.linalg.norm(direction_from_sphere))
            color = 255 * ((normal + 1) / 2)
            self.color = color
            return True

        self.steps += 1
        if self.steps >= self.lifetime:
            return True
        return False

        

    def is_finished(self):
        return True

    def get_color(self):
        
        return self.color
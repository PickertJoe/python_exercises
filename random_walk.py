# A program to randomly generate a walk as modeled by Eric Matthes in "Python Crash Course"

from random import choice


class Random_Walk():
    """A class to simulate the random movement of a particle"""

    def __init__(self, steps=5000):
        """Initializing the particle with n number of steps"""
        self.x_location = [0]
        self.y_location = [0]
        self.steps = steps

    def fill_walk(self):
        """Generating the movement behavior of the random walk"""

        while len(self.x_location) < self.steps:
            # Movement behavior in the x direction
            x_dir = choice([1, -1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist

            # Movement behavior in the y direction
            y_dir = choice([1, -1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dist * y_dir

            # Omitting steps that move nowehere
            if x_step == 0 and y_step == 0:
                continue

            # Adding the newly calculated step to the previous location
            new_x = self.x_location[-1] + x_step
            new_y = self.y_location[-1] + y_step

            # Adding the new location to the record of previous locations
            self.x_location.append(new_x)
            self.y_location.append(new_y)

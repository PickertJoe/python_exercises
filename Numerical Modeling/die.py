# A module to contain the Die class

from random import randint


class Die():
    """Simulates the behavior of one rolled die"""

    def __init__(self, sides=6):
        """Creating a six sided die"""
        self.sides = sides

    def roll(self):
        """Simulating the action of rolling"""
        return randint(1, self.sides)

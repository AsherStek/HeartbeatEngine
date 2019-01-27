# Import the inherited class
import BoundingBox

# Base class for any Entity such as a player or mob
class Entity(BoundingBox.BoundingBox):
    def __init__(self, x, y, width, height, name):
        super(Entity, self).__init__(x, y, width, height)
        self._name = name

    # Getters
    @property
    def name(self):
        return self._name

    # Setters
    @name.setter
    def name(self, string):
        self._name = string
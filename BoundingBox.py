# Base class for every object that has some form of collision/sprite
class BoundingBox(object):
    def __init__(self, x, y, width, height):
        self._x1 = x
        self._y1 = y
        self._width = width
        self._height = height

    # Getters
    @property
    def x1(self):
        return self._x1
    @property
    def y1(self):
        return self._y1
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    # Setters
    @x1.setter
    def x1(self, value):
        self._x1 = value
    @y1.setter
    def y1(self, value):
        self._y1 = value
    @width.setter
    def width(self, value):
        self._width = value
    @height.setter
    def height(self, value):
        self._height = value
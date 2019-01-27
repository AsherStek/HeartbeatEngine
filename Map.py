class Map(object):
    def __init__(self, _rows, _columns, _x, _y, _size):
        self.rows = _rows
        self.columns = _columns
        self.x = _x
        self.y = _y
        self.size = _size

        self.spaces = []

        for row in range(self.rows):
            for column in range(self.columns):
                self.spaces.append([self.x + (row * self.size), self.y + (column * self.size)])

    def testPrint(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.spaces[row + (self.columns * column)], end="", flush=True)
            print()
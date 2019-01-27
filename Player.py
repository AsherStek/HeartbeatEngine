# Import inherited class
import Entity

# Player class containing all player unique commands
class Player(Entity.Entity):
    def __init__(self, x, y, width, height, name):
        super(Player, self).__init__(x, y, width, height, name)
        self.activeMap = None

    # Place player into a map
    def placeInMap(self, newMap):
        self.activeMap = newMap
        self.x1 = self.activeMap.x
        self.y1 = self.activeMap.y

    # Movement Switch Case
    def move(self, direction):
        dirs = {
            'w' : self.up,
            's' : self.down,
            'a' : self.left,
            'd' : self.right
        }
        cmd = dirs.get(direction)
        cmd()
        print("X1: {} Y1: {}".format(self.x1, self.y1))

    # Movement Functions
    def up(self):
        if (self.y1 - self.activeMap.size < 0):
            self.y1 = self.activeMap.y
        else:
            self.y1 -= self.activeMap.y
    def down(self):
        if (self.y1 + self.activeMap.size > self.activeMap.columns * self.activeMap.y):
            self.y1 = self.activeMap.columns * self.activeMap.y
        else:
            self.y1 += self.activeMap.size
    def left(self):
        if (self.x1 - self.activeMap.size < 0):
            self.x1 = self.activeMap.x
        else:
            self.x1 -= self.activeMap.size
    def right(self):
        if (self.x1 + self.activeMap.size > self.activeMap.rows * self.activeMap.x):
            self.x1 = self.activeMap.rows * self.activeMap.x
        else:
            self.x1 += self.activeMap.size
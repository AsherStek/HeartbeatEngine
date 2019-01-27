# Import everything needed for the engine as well as in game objects
import time as t
import tkinter as tk
import Map as m
import Player as p
import KeyboardCallbacks as k

class HeartBeat(object):
    # Create Map
    mp = m.Map(3,3, 254, 254, 32)

    # Create a keyboard class
    keyCalls = k.KeyboardCallbacks()

    # Dictionaries that will contain every active object and sprite
    objects = {}
    sprites = {}

    # Important variables for the engine
    throttle = 10000
    million = 1000000
    billion = 1000000000

    lastFpsTime = 0
    fps = 0

    # The engine
    def run(self, running, window, canvas):

        # Initialize all active objects and respective sprites here
        self.createObjects(p.Player(0,0,32,32,'Player'))
        self.createSprites(self.objects['{}'.format('Player')], canvas)

        # Initialize all keyboard bindings
        self.createBindings(window, self.objects['Player'])

        # Init player position
        self.objects['Player'].placeInMap(self.mp)

        # More engine variables
        lastLoopTime = self.nanoTime()
        TARGET_FPS = 15
        OPTIMAL_TIME = self.billion / TARGET_FPS

        # Contain this in a try loop to bypass stack trace on close
        try:
            
            # The actual game loop
            while (running):
                now = self.nanoTime()
                updateLength = now - lastLoopTime
                lastLoopTime = now
                delta = float(updateLength / OPTIMAL_TIME)
                self.lastFpsTime += (updateLength * self.billion)
                self.fps += 1
                if (self.lastFpsTime >= self.billion/self.throttle):
                    self.lastFpsTime = 0
                    self.fps = 0
                
                # All game updates and rendering is done here
                self.update(delta)
                self.render(delta, canvas)

                sleepFor = int((lastLoopTime - self.nanoTime() + OPTIMAL_TIME)/self.million)
                if (sleepFor < 0):
                    sleepFor *= -1
                t.sleep(1/1/sleepFor)
                window.update_idletasks()
                window.update()
        except tk.TclError:
            print("Program either was closed or unexpectedly failed")

    # Game Logic
    def update(self, delta):
        pass

    # Game rendering
    def render(self, delta, canvas):
        for key in self.objects.values():
            canvas.coords(self.sprites[key.name], key.x1, key.y1, key.x1 + key.width, key.y1 + key.height)

    # Object Initializer
    def createObjects(self, entity):
        self.objects['{}'.format(entity.name)] = entity

    # Sprite Initializer
    def createSprites(self, entity, canvas):
        self.sprites['{}'.format(entity.name)] = canvas.create_rectangle(entity.x1, entity.y1, entity.x1 + entity.width, entity.y1 + entity.height, fill='red')

    # Keyboard Initializer
    def createBindings(self, window, player):
        window.bind("<Escape>", lambda e, win=window: self.keyCalls.quitOut(e, win))
        window.bind("<KeyPress-w>", lambda e, p=player: self.keyCalls.playerMove(e, p))
        window.bind("<KeyPress-s>", lambda e, p=player: self.keyCalls.playerMove(e, p))
        window.bind("<KeyPress-a>", lambda e, p=player: self.keyCalls.playerMove(e, p))
        window.bind("<KeyPress-d>", lambda e, p=player: self.keyCalls.playerMove(e, p))

    # Nanotime for engine
    def nanoTime(self):
        return ((1000 * t.perf_counter()) /10000) * 100

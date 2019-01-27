# Import the Graphics library and the engine
import tkinter as tk
import Heartbeat as h

class Window(object):

    # Create a new Heartbeat engine
    heart = h.HeartBeat()

    # Initialize all window values and start the engine
    def __init__(self, width_, height_):
        self.width = width_
        self.height = height_
        
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.root.resizable(0,0)
        self.root.title("A Real Time Tkinter Game Test")
        self.can = tk.Canvas(self.root, width=self.width, height=self.height, bg='white')
        self.can.grid(row=0, column=0)

        self.heart.run(True, self.root, self.can)
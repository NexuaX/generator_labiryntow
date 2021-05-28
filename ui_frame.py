# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#         UI Class          #
# ************************* #

from tkinter import *
import tkinter as tk

if __name__ == "__main__":
    print("Not a program!")
    exit()

print(__name__, "imported")

class AppFrame(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        self.master = master
        self.master.title("Generator labiryntów by AM")
        self.prepare_grid()
    def prepare_grid(self):
        self.menu = tk.Frame(width=200, height=600, background="red")
        self.maze = tk.Frame(width=600, height=600, background="blue")
        self.menu.pack(side=tk.LEFT)
        self.maze.pack(side=tk.RIGHT)

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
        self.prepare_menu()
        self.prepare_maze()
    def prepare_grid(self):
        self.menu = tk.Frame(width=600, height=200, background="red")
        self.maze = tk.Frame(width=600, height=600, background="blue")
        self.menu.grid(row=0)
        self.maze.grid(row=1)
    def prepare_menu(self):
        self.xparam_label = tk.Label(
            master=self.menu,
            text="X SIZE:"
        )
        self.yparam_label = tk.Label(
            master=self.menu,
            text="Y SIZE:"
        )
        self.xparam_entry = tk.Spinbox(
            master=self.menu,
            from_=10,
            to=30,
            width=3
        )
        self.yparam_entry = tk.Spinbox(
            master=self.menu,
            from_=10,
            to=30,
            width=3
        )
        self.generate_btn = tk.Button(
            master=self.menu,
            text="Generate!",
            command=self.generate_btn_handler
        )
        self.menu.columnconfigure([0,1], minsize=100)
        self.menu.columnconfigure(2, minsize=400)
        self.xparam_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.xparam_entry.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.yparam_label.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        self.yparam_entry.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        self.generate_btn.grid(row=0, column=2, rowspan=2, sticky="e", padx=10)
    def prepare_maze(self, x=10, y=10):
        self.maze_grid = []
        for i in range(x):
            self.maze_grid.append(list())
            for j in range(y):
                self.maze_grid[i].append(
                    tk.Button(
                        master=self.maze,
                        text=f"{i} {j}"
                        )
                    )
                self.maze_grid[i][j].grid(row=i, column=j)
    
    def generate_btn_handler(self):
        x = int(self.xparam_entry.get())
        y = int(self.yparam_entry.get())
        for row in self.maze_grid:
            for item in row:
                item.destroy()
        self.prepare_maze(x, y)
        


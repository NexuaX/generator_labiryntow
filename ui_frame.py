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
    def __init__(self, main, master=tk.Tk()):
        super().__init__(master)
        self.main = main
        self.master = master
        self.master.title("Generator labiryntów by AM")
        self.prepare_grid()
        self.prepare_menu()
        self.prepare_maze()
        self.start_end = [0, 0]

    def prepare_grid(self):
        self.menu = tk.Frame(width=600, height=200)
        self.maze = tk.Frame(width=600, height=600)
        self.menu.grid(row=0)
        self.maze.grid(row=1)

    def prepare_menu(self):
        self.xparam_label = tk.Label(
            master=self.menu,
            text="X SIZE:")
        self.yparam_label = tk.Label(
            master=self.menu,
            text="Y SIZE:")
        self.xparam_entry = tk.Spinbox(
            master=self.menu,
            from_=10,
            to=30,
            width=3)
        self.yparam_entry = tk.Spinbox(
            master=self.menu,
            from_=10,
            to=30,
            width=3)
        self.generate_btn = tk.Button(
            master=self.menu,
            text="Generate!",
            command=self.generate_btn_handler)
        self.prepare_btn = tk.Button(
            master=self.menu,
            text="Prepare",
            command=self.prepare_btn_handler)
        self.menu.columnconfigure([0,1], minsize=50)
        self.menu.columnconfigure([2,3], minsize=100)
        self.xparam_label.grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.xparam_entry.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.yparam_label.grid(row=0, column=1, sticky="w", padx=5, pady=2)
        self.yparam_entry.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        self.generate_btn.grid(row=0, column=3, rowspan=2, sticky="e", padx=10)
        self.prepare_btn.grid(row=0, column=2, rowspan=2, sticky="e", padx=10)

    def prepare_maze(self, x=10, y=10):
        line_width = 2
        size = 15+line_width
        self.maze_grid = tk.Canvas(
            master=self.maze,
            width=x*size+line_width,
            height=y*size+line_width,
            background="black")
        self.maze_grid.ids = []
        self.maze_grid.x = x
        self.maze_grid.y = y
        for i in range(x):
            self.maze_grid.ids.append(list())
            for j in range(y):
                idr = self.maze_grid.create_rectangle(
                    i*size+2*line_width, j*size+2*line_width,
                    (i+1)*size+line_width, (j+1)*size+line_width,
                    fill="blue",
                    width=0,
                    tag=(f"{i},{j}", "cell"))
                self.maze_grid.ids[i].append(idr)
        for i in range(x):
            self.maze_grid.tag_bind(self.maze_grid.ids[i][0], "<Button-1>", self.pick_start_rect_handler)
            self.maze_grid.tag_bind(self.maze_grid.ids[i][y-1], "<Button-1>", self.pick_start_rect_handler)
            self.maze_grid.addtag_withtag("border_cell", self.maze_grid.ids[i][0])
            self.maze_grid.addtag_withtag("border_cell", self.maze_grid.ids[i][y-1])
        for i in range(1, y-1):
            self.maze_grid.tag_bind(self.maze_grid.ids[0][i], "<Button-1>", self.pick_start_rect_handler)
            self.maze_grid.tag_bind(self.maze_grid.ids[x-1][i], "<Button-1>", self.pick_start_rect_handler)
            self.maze_grid.addtag_withtag("border_cell", self.maze_grid.ids[0][i])
            self.maze_grid.addtag_withtag("border_cell", self.maze_grid.ids[x-1][i])
        for i in range(1, x-1):
            for j in range(1, y-1):
                self.maze_grid.addtag_withtag("inside", self.maze_grid.ids[i][j])
        self.maze_grid.pack()

    def prepare_btn_handler(self):
        x = int(self.xparam_entry.get())
        y = int(self.yparam_entry.get())
        self.maze_grid.destroy()
        self.prepare_maze(x, y)
        
    def generate_btn_handler(self):
        self.maze_grid.destroy()
        self.prepare_maze(self.maze_grid.x, self.maze_grid.y)
        self.main.run_generator(self.maze_grid.x, self.maze_grid.y, self.maze_grid.ids)

    def pick_start_rect_handler(self, event):
        idr = self.maze_grid.find_closest(event.x, event.y)
        self.start_end[0] = self.maze_grid.gettags(idr)[0]
        self.maze_grid.itemconfigure(idr, fill="green")
        for idr in self.maze_grid.find_withtag("border_cell"):
            self.maze_grid.tag_bind(idr, "<Button-1>", self.pick_end_rect_handler, False)

    def pick_end_rect_handler(self, event):
        idr = self.maze_grid.find_closest(event.x, event.y)
        self.start_end[1] = self.maze_grid.gettags(idr)[0]
        self.maze_grid.itemconfigure(idr, fill="orange")
        for idr in self.maze_grid.find_withtag("border_cell"):
            self.maze_grid.tag_unbind(idr, "<Button-1>")

    def pick_pivot_rect_handler(self, event):
        pass
        
# def rect_handler(event, idr=idr):
#                     event.widget.itemconfigure(idr, fill="white")
#                 self.maze_grid.tag_bind(idr, "<Button-1>", rect_handler)
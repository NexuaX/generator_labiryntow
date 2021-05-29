# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#      Generator Class      #
# ************************* #

import random
import time

if __name__ == "__main__":
    print("Not a program!")
    exit()

print(__name__, "imported")

class Cell:
    def __init__(self, x, y, idr, walls = ("n", "e", "s", "w")):
        self.x = x
        self.y = y
        self.idr = idr
        self.walls = walls

class Generator:
    def __init__(self, main, x, y, ids, start_end):
        self.main = main
        self.x = x
        self.y = y
        self.ids = ids
        self.start_end = start_end
    
    def generate(self):
        self.prepare_cells()
        stack = list()
        visited = list()
        path = list()
        start = tuple(self.start_end[0].split(","))
        start = (int(start[0]), int(start[1]))
        end = tuple(self.start_end[1].split(","))
        end = (int(end[0]), int(end[1]))
        stack.append(start)
        visited.append(start)
        line_width = 2
        size = 15+line_width
        direction = ""
        while len(visited) < self.x*self.y:
            input()
            current = stack[-1]
            walls = self.cells[current[0]][current[1]].walls
            for direction in random.sample(walls, len(walls)):
                if direction == "n":
                    if (current[0], current[1]-1) not in visited:
                        current = (current[0], current[1]-1)
                        break
                elif direction == "s":
                    if (current[0], current[1]+1) not in visited:
                        current = (current[0], current[1]+1)
                        break
                elif direction == "e":
                    if (current[0]+1, current[1]) not in visited:
                        current = (current[0]+1, current[1])
                        break
                elif direction == "w":
                    if (current[0]-1, current[1]) not in visited:
                        current = (current[0]-1, current[1])
                        break
            else:
                stack.pop()
                continue
            stack.append(current)
            visited.append(current)
            cell = self.cells[current[0]][current[1]]
            self.main.ui.maze_grid.itemconfigure(cell.idr, fill="white")
            if direction == "n":
                self.main.ui.maze_grid.create_line(
                    current[0]*size+2*line_width, current[1]*size+size+line_width+1,
                    current[0]*size+size+line_width, current[1]*size+size+line_width+1,
                    fill="white", width=2)
            elif direction == "s":
                self.main.ui.maze_grid.create_line(
                    current[0]*size+2*line_width, current[1]*size+line_width+1,
                    current[0]*size+size+line_width, current[1]*size+line_width+1,
                    fill="white", width=2)
            elif direction == "e":
                self.main.ui.maze_grid.create_line(
                    current[0]*size+2*line_width-1, current[1]*size+2*line_width,
                    current[0]*size+2*line_width-1, current[1]*size+size+line_width,
                    fill="white", width=2)
            elif direction == "w":
                self.main.ui.maze_grid.create_line(
                    current[0]*size+size+2*line_width-1, current[1]*size+2*line_width,
                    current[0]*size+size+2*line_width-1, current[1]*size+size+line_width,
                    fill="white", width=2)
        if end[0] == 0:
            self.main.ui.maze_grid.create_line(
                2*line_width-1, end[1]*size+2*line_width,
                2*line_width-1, end[1]*size+size+line_width,
                fill="white", width=2)
        elif end[0] == self.x-1:
            self.main.ui.maze_grid.create_line(
                self.x*size+2*line_width-1, end[1]*size+2*line_width,
                self.x*size+2*line_width-1, end[1]*size+size+line_width,
                fill="white", width=2)
        elif end[1] == 0:
            self.main.ui.maze_grid.create_line(
                end[0]*size+2*line_width, line_width+1,
                end[0]*size+size+line_width, line_width+1,
                fill="white", width=2)
        elif end[1] == self.y-1:
            self.main.ui.maze_grid.create_line(
                end[0]*size+2*line_width, self.y*size+line_width+1,
                end[0]*size+size+line_width, self.y*size+line_width+1,
                fill="white", width=2)
            
    def prepare_cells(self):
        self.cells = list()
        for i in range(self.x):
            self.cells.append(list())
            for j in range(self.y):
                self.cells[i].append(Cell(i, j, self.ids[i][j]))
        for i in range(1, self.x - 1):
            self.cells[i][0].walls = ("e", "s", "w")
        for i in range(1, self.x - 1):
            self.cells[i][self.y-1].walls = ("e", "n", "w")
        for i in range(1, self.y - 1):
            self.cells[0][i].walls = ("e", "s", "n")
        for i in range(1, self.y - 1):
            self.cells[self.x - 1][i].walls = ("s", "n", "w")
        self.cells[0][0].walls = ("s", "e")
        self.cells[self.x-1][0].walls = ("s", "w")
        self.cells[0][self.y-1].walls = ("n", "e")
        self.cells[self.x-1][self.y-1].walls = ("n", "w")


        




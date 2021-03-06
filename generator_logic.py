# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#      Generator Class      #
# ************************* #

import random

# NIE ODPALAMY JAKO PROGRAM
if __name__ == "__main__":
    print("Not a program!")
    exit()

# INFORMACJA DEBUGUJĄCA
print(__name__, "imported")

class Cell:
    """Klasa pomocnicza do przechowowyania informacji o komórkach labiryntu"""
    def __init__(self, x, y, idr, walls = ("n", "e", "s", "w")):
        self.x = x
        self.y = y
        self.idr = idr
        self.walls = set(walls)
        self.moves = set()

class Generator:
    """Klasa Generator do generacji zadanego parametrami labiryntu"""
    def __init__(self, main, x, y, ids, start_end):
        """Konstruktor inicjalizujący wartości generatora"""
        self.main = main
        self.x = x
        self.y = y
        self.ids = ids
        self.start_end = start_end
        self.path = list()
        self.directions = list()
    
    def generate(self, pivots):
        """Funkcja pośrednia w generacji labiryntu, validuje wprowadzone dane do klasy
        oraz upewnia się że wygenerowany labirynt spełnia wymagania."""
        if 10 > self.x or self.x > 25:
            raise ValueError("Invalid dimentions!")
        if 10 > self.y or self.y > 25:
            raise ValueError("Invalid dimentions!")
        for index, pivot in enumerate(pivots):
            cell = tuple(pivot.split(","))
            pivots[index] = (int(cell[0]), int(cell[1]))
        flag1, flag2 = True, True
        while flag1 or flag2:
            flag1, flag2 = True, True
            self.main.ui.maze_grid.destroy()
            self.main.ui.prepare_maze(self.x, self.y)
            self.__generate()
            for elem in pivots:
                if elem not in self.path:
                    break
            else:
                flag1 = False
            if len(self.path) > max((self.x, self.y)):
                flag2 = False
            
    def __generate(self):
        """Wewnętrzna funkcja generująca jeden labirynt"""
        self.prepare_cells()
        stack = list()
        visited = list()
        start = tuple(self.start_end[0].split(","))
        start = (int(start[0]), int(start[1]))
        end = tuple(self.start_end[1].split(","))
        end = (int(end[0]), int(end[1]))
        if start == end:
            raise ValueError("start and end are the same!")
        stack.append(start)
        visited.append(start)
        direction = ""
        directions = list()
        while len(visited) < self.x*self.y:
            #input()
            current = stack[-1]
            cell = self.cells[current[0]][current[1]]
            walls = cell.walls
            for direction in random.sample(walls, len(walls)):
                if direction == "n":
                    if (current[0], current[1]-1) not in visited:
                        current = (current[0], current[1]-1)
                        cell.moves.add("n")
                        break
                elif direction == "s":
                    if (current[0], current[1]+1) not in visited:
                        current = (current[0], current[1]+1)
                        cell.moves.add("s")
                        break
                elif direction == "e":
                    if (current[0]+1, current[1]) not in visited:
                        current = (current[0]+1, current[1])
                        cell.moves.add("e")
                        break
                elif direction == "w":
                    if (current[0]-1, current[1]) not in visited:
                        current = (current[0]-1, current[1])
                        cell.moves.add("w")
                        break
            else:
                stack.pop()
                directions.pop()
                if random.random() < 0.1:
                    self.clear_wall(current, random.sample(walls, 1))
                continue
            stack.append(current)
            visited.append(current)
            directions.append(direction)
            if current == end:
                self.path = stack.copy()
                self.directions = directions.copy()
            self.color_cell(current, "white", direction)

        line_width = 2
        size = 15+line_width
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

        self.draw_path()
            
    def prepare_cells(self):
        """Funckja przygotowywująca elementy klasy Cell do generacji labiryntu"""
        self.cells = list()
        for i in range(self.x):
            self.cells.append(list())
            for j in range(self.y):
                self.cells[i].append(Cell(i, j, self.ids[i][j]))
        for i in range(1, self.x - 1):
            self.cells[i][0].walls = set(("e", "s", "w"))
        for i in range(1, self.x - 1):
            self.cells[i][self.y-1].walls = set(("e", "n", "w"))
        for i in range(1, self.y - 1):
            self.cells[0][i].walls = set(("e", "s", "n"))
        for i in range(1, self.y - 1):
            self.cells[self.x - 1][i].walls = set(("s", "n", "w"))
        self.cells[0][0].walls = set(("s", "e"))
        self.cells[self.x-1][0].walls = set(("s", "w"))
        self.cells[0][self.y-1].walls = set(("n", "e"))
        self.cells[self.x-1][self.y-1].walls = set(("n", "w"))

    def color_cell(self, current, color, direction):
        """Zaznaczenie które elementy stają się aktualnie tunelem"""
        idr = self.cells[current[0]][current[1]].idr
        obj = self.main.ui.maze_grid.find_withtag("pivot")
        if idr not in obj:
            self.main.ui.maze_grid.itemconfigure(idr, fill=color)
        line_width = 2
        size = 15+line_width
        if direction == "n":
            self.main.ui.maze_grid.create_line(
                current[0]*size+2*line_width, current[1]*size+size+line_width+1,
                current[0]*size+size+line_width, current[1]*size+size+line_width+1,
                fill=color, width=2)
        elif direction == "s":
            self.main.ui.maze_grid.create_line(
                current[0]*size+2*line_width, current[1]*size+line_width+1,
                current[0]*size+size+line_width, current[1]*size+line_width+1,
                fill=color, width=2)
        elif direction == "e":
            self.main.ui.maze_grid.create_line(
                current[0]*size+2*line_width-1, current[1]*size+2*line_width,
                current[0]*size+2*line_width-1, current[1]*size+size+line_width,
                fill=color, width=2)
        elif direction == "w":
            self.main.ui.maze_grid.create_line(
                current[0]*size+size+2*line_width-1, current[1]*size+2*line_width,
                current[0]*size+size+2*line_width-1, current[1]*size+size+line_width,
                fill=color, width=2)
        pass

    def draw_path(self):
        """Funckja tworząca ścierzkę do celu w labiryncie"""
        for i in range(len(self.path) - 1):
            self.color_cell(self.path[i+1], "cyan", self.directions[i])
        pass

    def clear_wall(self, current, direction):
        """Dodatkowa funkcja dla labiryntu która wywołana usuwa
        losową ścianę w celu urozmaicenia labiryntu, może zostać pominięta"""
        line_width = 2
        size = 15+line_width
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
        pass

    






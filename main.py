# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#      Program  główny      #
# ************************* #

import generator_logic as gl
import ui_frame as ui

if __name__ != '__main__':
    print("Don't import as module!")
    exit()

class MainApp:
    def __init__(self):
        self.ui = ui.AppFrame(self)
    def start(self):
        self.ui.mainloop()
    def run_generator(self, x, y, ids):
        self.gl = gl.Generator(self, x, y, self.ui.maze_grid.ids, self.ui.start_end)
        self.gl.generate()

app = MainApp()
app.start()

# ************************* #
#    Generator Labirytów    #
#      Albert Mouhoubi      #
#      Program  główny      #
# ************************* #

import generator_logic as gl
import ui_frame as ui

class MainApp:
    """Główna klasa sterująca aplikacją, startuje UI oraz
    zapewnia połączenie między UI a Generatorem."""
    def __init__(self):
        self.ui = ui.AppFrame(self)
    def start(self):
        self.ui.mainloop()
    def run_generator(self, x, y, ids, pivots):
        self.gl = gl.Generator(self, x, y, self.ui.maze_grid.ids, self.ui.start_end)
        self.gl.generate(pivots)

# Aplikacja automatycznie się otwiera gdy
# odpalimy skrypt jako main (nie import)
# tak jak w testach
if __name__ == '__main__':
    app = MainApp()
    app.start()

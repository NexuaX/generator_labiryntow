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
        self.ui = ui.AppFrame()
    def start(self):
        self.ui.mainloop()

app = MainApp()
app.start()

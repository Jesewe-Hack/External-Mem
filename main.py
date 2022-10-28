from utils.getGame import *
from utils.getUpdate import *
from utils.rh import *
from utils.wh import *
from utils.about import *

import pymem, re
import pymem.process
import keyboard
import version
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui.ui")

check_update_app()
check_game_connection()
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# clicked buttons [Update 1.6]
form.pushButton.clicked.connect(wallhack_thread)
form.pushButton_2.clicked.connect(radar_thread)
# clicked buttons [Update 1.7]
form.pushButton_3.clicked.connect(about)

# key binds [Update 1.7]
keyboard.add_hotkey('f5', wallhack_thread)
keyboard.add_hotkey('f6', radar_thread)

app.exec()
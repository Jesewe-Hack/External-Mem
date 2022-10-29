from utils.getGame import *
from utils.rh import *
from utils.wh import *
from utils.about import *
from utils.settings import *
from utils.money import *

import pymem, re
import pymem.process
import keyboard
import version
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("gui.ui")

check_game_connection()
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.pushButton.clicked.connect(wallhack_thread)
form.pushButton_2.clicked.connect(radar_thread)
form.pushButton_3.clicked.connect(about)
form.pushButton_4.clicked.connect(settings)
form.pushButton_5.clicked.connect(money_thread)

# key binds
keyboard.add_hotkey('f5', wallhack_thread)
keyboard.add_hotkey('f6', radar_thread)
keyboard.add_hotkey('f7', money_thread)

app.exec()
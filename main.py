from utils.getGame import *
from utils.getUpdate import *
from utils.rh import *
from utils.wh import *

import pymem, re
import pymem.process
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

form.pushButton.clicked.connect(wallhack_thread)
form.pushButton_2.clicked.connect(radar_thread)

app.exec()
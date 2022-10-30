from utils.getGame import *
from utils.rh import *
from utils.wh import *
from utils.money import *
from utils.about import *
from utils.settings import *
from utils.exit import *

import pymem, re
import pymem.process
import keyboard
import version
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from tkinter import messagebox

Form, Window = uic.loadUiType("gui.ui")

check_game_connection()
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.pushButton.clicked.connect(wallhack)
form.pushButton_2.clicked.connect(radarhack)
form.pushButton_3.clicked.connect(about)
form.pushButton_4.clicked.connect(settings)
form.pushButton_5.clicked.connect(money_reveal)

# key binds, you can edit keybinds in config.ini !
keyboard.add_hotkey('F4', wallhack_key)
keyboard.add_hotkey('F5', radarhack_key)
keyboard.add_hotkey('F6', money_key)
keyboard.add_hotkey('F10', exit)
	
app.exec()
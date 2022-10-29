from utils.tempcleaner import *
from utils.websites import *
from utils.getUpdate import *

import platform
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

def settings():
    Form, Window = uic.loadUiType("settings.ui")
    global window
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    form.temp_cleaner.clicked.connect(temp_cleaner)
    form.find_error.clicked.connect(find_error)
    form.check_update.clicked.connect(check_update_app)

    form.label_3.setText(f'Operating system: {platform.system()}\nPlatform type: {platform.platform()}\nComputer network name: {platform.node()}\nMachine type: {platform.machine()}')
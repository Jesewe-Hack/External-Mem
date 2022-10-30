from utils.tempcleaner import *
from utils.websites import *
from utils.getUpdate import *

import platform, socket, uuid, psutil, re
from datetime import datetime
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

    form.label_3.setText(f'System: {platform.system()}\nNode Name: {platform.node()}\nVersion: {platform.version()}\nMachine: {platform.machine()}\nPhysical cores: {psutil.cpu_count(logical=False)}\nTotal cores: {psutil.cpu_count(logical=True)}\n\nIP Address: {socket.gethostbyname(socket.gethostname())}')
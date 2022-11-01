from utils.rh import *
from utils.wh import *
from utils.money import *
from utils.about import *
from utils.exit import *
from utils.tempcleaner import *
from utils.websites import *
from utils.getUpdate import *

import platform, socket, uuid, psutil, re, version, keyboard, sys
from datetime import datetime
from tkinter import messagebox
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

#load both ui file
uifile_1 = 'home.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'about.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

uifile_3 = 'settings.ui'
form_3, base_3 = uic.loadUiType(uifile_3)

class Home(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.change)
        self.pushButton_4.clicked.connect(self.change2)
        self.pushButton.clicked.connect(wallhack)
        self.pushButton_2.clicked.connect(radarhack)
        self.pushButton_5.clicked.connect(money_reveal)

    def change(self):
        self.main = About()
        self.main.show()
        self.close()

    def change2(self):
        self.main = Settings()
        self.main.show()
        self.close()

class About(base_2, form_2):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.change)
        self.pushButton_4.clicked.connect(self.change2)
        self.pushButton_5.clicked.connect(website)
        self.pushButton_7.clicked.connect(github)
        self.pushButton_8.clicked.connect(twitter)

    def change(self):
        self.main = Home()
        self.main.show()
        self.close()

    def change2(self):
        self.main = Settings()
        self.main.show()
        self.close()

class Settings(base_3, form_3):
    def __init__(self):
        super(base_3, self).__init__()
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.change)
        self.pushButton_3.clicked.connect(self.change2)
        self.temp_cleaner.clicked.connect(temp_cleaner)
        self.find_error.clicked.connect(find_error)
        self.check_update.clicked.connect(check_update_app)
        self.label_4.setText(f'System: {platform.system()}\nNode Name: {platform.node()}\nVersion: {platform.version()}\nPhysical cores: {psutil.cpu_count(logical=False)}\nTotal cores: {psutil.cpu_count(logical=True)}\n\nIP Address: {socket.gethostbyname(socket.gethostname())}')

    def change(self):
        self.main = Home()
        self.main.show()
        self.close()

    def change2(self):
        self.main = About()
        self.main.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Home()
    ex.show()
    keyboard.add_hotkey('F4', wallhack_key)
    keyboard.add_hotkey('F5', radarhack_key)
    keyboard.add_hotkey('F6', money_key)
    keyboard.add_hotkey('F10', exit)
    sys.exit(app.exec())
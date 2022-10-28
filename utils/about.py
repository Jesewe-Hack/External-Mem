import webbrowser
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

def github():
    webbrowser.open('https://github.com/Jesewe-Hack')

def website():
    webbrowser.open('https://jesewe.wixsite.com/jesewehack')
    
def about():
    Form, Window = uic.loadUiType("about.ui")
    global window
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    form.pushButton_3.clicked.connect(website)
    form.pushButton_4.clicked.connect(github)
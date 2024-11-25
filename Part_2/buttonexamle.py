from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMenu
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Button Example")
        self.createButton()

    def createButton(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100, 100, 100, 50)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/python.png"))
        btn.setIconSize(QSize(40, 40))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet("background-color:grey")
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
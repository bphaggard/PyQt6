from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Event Handling")
        self.createWidget()

    def createWidget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        btn.clicked.coonnect(self.clickedButton())
        self.label = QLabel("Default Text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clickedButton(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet("color:red")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
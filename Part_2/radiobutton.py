from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("PyQt6 QRadio Button")

        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()

        radio1 = QRadioButton("Python")
        radio1.setIcon(QIcon("images/python.png"))
        radio1.setIconSize(QSize(40, 40))
        radio1.setFont(QFont("Times", 14))
        radio1.toggled.connect(self.radio_selected)

        radio2 = QRadioButton("Kotlin")
        radio2.setIcon(QIcon("images/kotlin.png"))
        radio2.setIconSize(QSize(40, 40))
        radio2.setFont(QFont("Times", 14))
        radio2.toggled.connect(self.radio_selected)

        radio3 = QRadioButton("Swift")
        radio3.setIcon(QIcon("images/swift.png"))
        radio3.setIconSize(QSize(40, 40))
        radio3.setFont(QFont("Times", 14))
        radio3.toggled.connect(self.radio_selected)

        self.label  =QLabel("")
        self.label.setFont(QFont("Sanserif", 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        hbox.addWidget(radio3)

        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText("You have selected : {} ".format(radio_btn.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
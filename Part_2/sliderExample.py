from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QHBoxLayout, QLabel, QComboBox, QSlider
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle("PyQt6 QSlider")

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.change_slider)

        vbox = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(QFont("Timer", 15))

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(vbox)

    def change_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
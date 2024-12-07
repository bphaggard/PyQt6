from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QCalendarWidget")

        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel("Calendar")
        self.label.setFont(QFont("Times", 15))

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calendar_date(self):
        date_selected = self.calendar.selectedDate()
        date_string = str(date_selected.toPyDate())

        self.label.setText("Date Is {} : ".format(date_string))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
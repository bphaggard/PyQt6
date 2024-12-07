from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")

        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        table_widget.setItem(0, 2, QTableWidgetItem("Phone"))

        table_widget.setItem(1, 0, QTableWidgetItem("Patrik"))
        table_widget.setItem(1, 1, QTableWidgetItem("name@gmail.com"))
        table_widget.setItem(1, 2, QTableWidgetItem("+421607445789"))

        table_widget.setItem(2, 0, QTableWidgetItem("John"))
        table_widget.setItem(2, 1, QTableWidgetItem("john.doe@gmail.com"))
        table_widget.setItem(2, 2, QTableWidgetItem("+4207234057773"))

        vbox.addWidget(table_widget)

        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
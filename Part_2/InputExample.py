from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QDialog, \
    QHBoxLayout, QLineEdit, QPushButton, QInputDialog
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QInputDialog")
        self.create_dialog()


    def create_dialog(self):
        hbox = QHBoxLayout()

        label = QLabel("Choose Country: ")
        label.setFont(QFont("Times", 15))

        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(QFont("Times", 15))

        btn = QPushButton("Choose Country")
        btn.setFont(QFont("Times", 15))
        btn.clicked.connect(self.get_int)

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(btn)

        self.setLayout(hbox)

    def show_dialog(self):
        countries = [
            "Italy", "Germany", "Spain", "Belgium", "France", "Czech", "Poland", "Croatia",
            "United Kingdom", "United States", "Canada", "Sweden", "Finland"
        ]

        country,ok = QInputDialog.getItem(self, "Input Dialog", "List Of Countries", countries, 0, False)
        if ok and country:
            self.lineEdit.setText(country)

    def get_text(self):
        myText,ok = QInputDialog.getText(self, "Get Username", "Enter Your Name: ")
        if ok and myText:
            self.lineEdit.setText(myText)

    def get_int(self):
        myNumber,ok = QInputDialog.getInt(self, "Order Quantity", "Enter Quantity: ", 1, 2, 30, 50)
        if ok and myNumber:
            self.lineEdit.setText(str(myNumber))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
# Form implementation generated from reading ui file 'book_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 405)
        Dialog.setStyleSheet("QLabel{\n"
"color:purple\n"
"}")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(21, 210, 350, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(22, 112, 203, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(22, 12, 123, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(22, 37, 71, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        # Connection with function
        self.radioButton_1.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        # Connection with function
        self.radioButton_2.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        # Connection with function
        self.radioButton_3.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(22, 137, 136, 61))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        # Connection with function
        self.radioButton_4.toggled.connect(self.radio_selected)
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        # Connection with function
        self.radioButton_5.toggled.connect(self.radio_selected)
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        # Connection with function
        self.radioButton_6.toggled.connect(self.radio_selected)
        self.verticalLayout_2.addWidget(self.radioButton_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        selected1 = ""
        selected2 = ""

        if self.radioButton_1.isChecked() == True:
            selected1 = "Python"
        if self.radioButton_2.isChecked() == True:
            selected1 = "Kotlin"
        if self.radioButton_3.isChecked() == True:
            selected1 = "Swift"
        if self.radioButton_4.isChecked() == True:
            selected2 = "Debit/Credit Card"
        if self.radioButton_5.isChecked() == True:
            selected2 = "Paypal"
        if self.radioButton_6.isChecked() == True:
            selected2 = "Cash"
        self.label_3.setText("Chosen Book: " + selected1 + ", " + "Chosen Payment Method: " + selected2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Choose Your Payment Method"))
        self.label.setText(_translate("Dialog", "Choose Your Book"))
        self.radioButton_1.setText(_translate("Dialog", "Python"))
        self.radioButton_2.setText(_translate("Dialog", "Kotlin"))
        self.radioButton_3.setText(_translate("Dialog", "Swift"))
        self.radioButton_4.setText(_translate("Dialog", "Debit/Credit Card"))
        self.radioButton_5.setText(_translate("Dialog", "Paypal"))
        self.radioButton_6.setText(_translate("Dialog", "Cash"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
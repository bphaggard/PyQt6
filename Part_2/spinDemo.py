# Form implementation generated from reading ui file 'spinDemo.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 276)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_pen = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_pen.setObjectName("lineEdit_pen")
        self.horizontalLayout.addWidget(self.lineEdit_pen)
        self.spinBox = QtWidgets.QSpinBox(parent=Form)

        self.spinBox.editingFinished.connect(self.first_result)

        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.lineEdit_pen_price = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_pen_price.setObjectName("lineEdit_pen_price")
        self.horizontalLayout.addWidget(self.lineEdit_pen_price)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_sugar = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_sugar.setObjectName("lineEdit_sugar")
        self.horizontalLayout_2.addWidget(self.lineEdit_sugar)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Form)

        self.doubleSpinBox.editingFinished.connect(self.second_result)

        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.lineEdit_sugar_price = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_sugar_price.setObjectName("lineEdit_sugar_price")
        self.horizontalLayout_2.addWidget(self.lineEdit_sugar_price)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def first_result(self):
        penPrice = int(self.lineEdit_pen.text())
        totalPenPrice = self.spinBox.value() * penPrice
        self.lineEdit_pen_price.setText(str(totalPenPrice))

    def second_result(self):
        sugarPrice = int(self.lineEdit_sugar.text())
        totalSugarPrice = self.doubleSpinBox.value() * sugarPrice
        self.lineEdit_sugar_price.setText(str(totalSugarPrice))

        totalPenPrice = int(self.lineEdit_pen_price.text())

        totalAmount = totalPenPrice + totalSugarPrice

        self.label_result.setText("Total Price Is : {} ".format(totalAmount))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pen Price:"))
        self.label_2.setText(_translate("Form", "Sugar Price:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
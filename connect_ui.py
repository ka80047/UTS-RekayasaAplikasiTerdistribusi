from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 336)
        self.hostTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.hostTextEdit.setGeometry(QtCore.QRect(160, 40, 145, 30))
        self.hostTextEdit.setObjectName("hostTextEdit")
        self.portTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.portTextEdit.setGeometry(QtCore.QRect(160, 80, 145, 31))
        self.portTextEdit.setObjectName("portTextEdit")
        self.nameTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.nameTextEdit.setGeometry(QtCore.QRect(160, 120, 145, 31))
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(125, 170, 90, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hostname"))
        self.label_2.setText(_translate("Form", "Port"))
        self.label_3.setText(_translate("Form", "Name"))
        self.pushButton.setText(_translate("Form", "Connect"))

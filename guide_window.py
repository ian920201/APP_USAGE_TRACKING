import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("User Guide")
        Dialog.resize(400, 300)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 300, 150))
        self.label.setText("1. press \"Start Record\" to start recording<br>2. press \"Stop Record\" to stop recording<br>3. press \"Start Analysis\" to start data analysis")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("User Guide", "User Guide"))
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

from guide_window import Ui_Dialog 

class AnalysisThread(QtCore.QThread):
    analysis_finished = QtCore.pyqtSignal()

    def run(self):
        process = subprocess.Popen(["python", "analysis.py"])
        process.wait()
        self.analysis_finished.emit()

class Ui_MainWindow(object):
    def __init__(self):
        self.process = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Start Record")
        self.pushButton.clicked.connect(self.on_pushButton_click)
        self.horizontalLayout.addWidget(self.pushButton)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Start Analysis")
        self.pushButton_3.clicked.connect(self.on_pushButton_3_click)
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        self.guide = QtWidgets.QPushButton(self.centralwidget)
        self.guide.setObjectName("guide")
        self.guide.setText("Guide")
        self.guide.clicked.connect(self.on_guide_button_click)
        self.horizontalLayout.addWidget(self.guide)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please press guide for more information if needed."))

    def on_pushButton_click(self):
        if self.pushButton.text() == "Start Record":
            self.label.setText("Recording...")
            self.process = subprocess.Popen(["python", "test.py"])
            self.pushButton.setText("Stop Record")
        else:
            if self.process:
                self.process.terminate()
                self.process = None
                self.label.setText("Recording stopped.")
            self.pushButton.setText("Start Record")

    def on_pushButton_3_click(self):
        self.pushButton_3.setEnabled(False)
        self.label.setText("Analyzing...")
        self.analysis_thread = AnalysisThread()
        self.analysis_thread.analysis_finished.connect(self.on_analysis_finished)
        self.analysis_thread.start()

    def on_analysis_finished(self):
        self.pushButton_3.setEnabled(True)
        self.label.setText("Analysis completed.")

    def on_guide_button_click(self):
        self.dialog = QtWidgets.QDialog()
        self.guide_ui = Ui_Dialog()
        self.guide_ui.setupUi(self.dialog)
        self.dialog.exec_() 



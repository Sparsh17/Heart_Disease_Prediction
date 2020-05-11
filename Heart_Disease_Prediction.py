import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUi
import sys

# =========================================================================================================================================================================================================================================
# --------------------------------------------------------------------------GUI------------------------------------------------------------------------------------------------------------------------------------------------------------
# ==========================================================================================================================================================================================================================================



# Form implementation generated from reading ui file 'final/final1.ui'



class final1_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 884)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 861))
        self.label.setStyleSheet("filter: brightness(50%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Desktop/resize-15724115882069245767hearthealthover60.jpg"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 690, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: #000;\n"
"background-color: lightblue;\n"
"font: \"Open Sans\";")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
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
        self.label_3.setStyleSheet(_translate("MainWindow", "color:#000;\n"
"font: \"Open Sans\";"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Predict your chance of having a heart disease because prevention </span></p><p><span style=\" font-size:18pt;\">is better than cure!</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START NOW"))
        self.label_4.setStyleSheet(_translate("MainWindow", "color:#000;\n"
"font: \"Open Sans\";"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">HEART DISEASE PREDICTION SYSTEM</span></p></body></html>"))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================




# Form implementation generated from reading ui file 'final/final2.ui'


class final2_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 866)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 650, 201, 121))
        self.pushButton.setStyleSheet("background-color: #f4f4f4;\n"
"color: #dc143c;\n"
"font-size: 25px;\n"
"font: \"Open Sans\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 650, 201, 121))
        self.pushButton_2.setStyleSheet("background-color: #f4f4f4;\n"
"color: #dc143c;\n"
"font-size: 25px;\n"
"font: \"Open Sans\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 380, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1051, 501))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../testGui/bbb.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 490, 1051, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 650, 81, 241))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 650, 491, 241))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(966, 649, 91, 241))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 770, 201, 111))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(770, 770, 261, 111))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../testGui/ccc.jpg"))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 21))
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
        self.pushButton.setText(_translate("MainWindow", "NEW USER"))
        self.pushButton_2.setText(_translate("MainWindow", "OLD USER"))



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================



# Form implementation generated from reading ui file 'final/final3.ui'



class final3_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(290, 30, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: \"Open Sans\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 150, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: \"Open Sans\";")
        self.label_16.setObjectName("label_16")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 150, 171, 22))
        self.lineEdit.setStyleSheet("background-color:#fff;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 290, 171, 22))
        self.comboBox.setStyleSheet("background-color:#fff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 220, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: \"Open Sans\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(40, 290, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: \"Open Sans\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(40, 360, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font: \"Open Sans\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(40, 430, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("font: \"Open Sans\";")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(40, 500, 411, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font: \"Open Sans\";")
        self.label_21.setObjectName("label_21")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 220, 171, 22))
        self.lineEdit_2.setStyleSheet("background-color:#fff;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 360, 171, 22))
        self.lineEdit_3.setStyleSheet("background-color:#fff;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 430, 171, 22))
        self.lineEdit_4.setStyleSheet("background-color:#fff;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 500, 500, 50))
        self.lineEdit_5.setStyleSheet("background-color:#fff;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 620, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: \"Open Sans\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 21))
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
        self.label_15.setText(_translate("MainWindow", "Enter the details given below:"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Name:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Age:</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Gender:</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Mobile No.:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Email:</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Your Address:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================



# Form implementation generated from reading ui file 'finalgui/final4.ui'



class final4_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(880, 235, 171, 22))
        self.comboBox_2.setStyleSheet("background-color:#fff;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_11.setGeometry(QtCore.QRect(880, 415, 171, 22))
        self.comboBox_11.setStyleSheet("background-color:#fff;")
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 660, 721, 31))
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 325, 500, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 770, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(880, 145, 171, 22))
        self.lineEdit.setStyleSheet("background-color:#fff;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 235, 371, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(880, 460, 171, 22))
        self.lineEdit_8.setStyleSheet("background-color:#fff;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 460, 511, 31))
        self.label_8.setObjectName("label_8")
        self.comboBox_13 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_13.setGeometry(QtCore.QRect(880, 610, 171, 22))
        self.comboBox_13.setStyleSheet("background-color:#fff;")
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_12.setGeometry(QtCore.QRect(880, 506, 171, 22))
        self.comboBox_12.setStyleSheet("background-color:#fff;")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 370, 500, 31))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(70, 710, 721, 31))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(880, 555, 171, 22))
        self.lineEdit_9.setStyleSheet("background-color:#fff;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 280, 500, 31))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 506, 500, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(880, 190, 171, 22))
        self.comboBox.setStyleSheet("background-color:#fff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_14 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_14.setGeometry(QtCore.QRect(880, 660, 171, 22))
        self.comboBox_14.setStyleSheet("background-color:#fff;")
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 415, 500, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(880, 280, 171, 22))
        self.lineEdit_6.setStyleSheet("background-color:#fff;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 190, 271, 31))
        self.label.setObjectName("label")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(880, 325, 171, 22))
        self.lineEdit_7.setStyleSheet("background-color:#fff;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(360, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(70, 145, 371, 31))
        self.label_16.setObjectName("label_16")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 555, 721, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 610, 721, 31))
        self.label_11.setObjectName("label_11")
        self.comboBox_15 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_15.setGeometry(QtCore.QRect(880, 710, 171, 22))
        self.comboBox_15.setStyleSheet("background-color:#fff;")
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(880, 370, 171, 22))
        self.comboBox_10.setStyleSheet("background-color:#fff;")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(70, 100, 371, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(880, 100, 171, 22))
        self.lineEdit_2.setStyleSheet("background-color:#fff;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
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
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Typical Angina"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Atypical Angina"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Non Angina"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Asymptomatic Angina"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "normal"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "ST-T wave abnormality"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "left ventricular hypertrophy"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient ca (number of major vessels colored by fluoroscopy):</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient chol(serum cholestrol level):</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient cp(chest pain): </span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient thalach (maximum heart rate achieved):</span></p></body></html>"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "upsloping"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "flat"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "downsloping"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "No"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient fbs(fasting blood sugar): </span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient thal( thalassemia):</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient restbp(resting blood pressure):</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient exang (exercise induced angina):</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "3"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient restecg (resting electrocardiography):</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient Gender:</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Enter the details given below:"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient Age:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient oldpeak (ST depression induced by exercise relative to rest):</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient slope (slope of peak exercise ST segment):</span></p></body></html>"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "normal"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "fixed defect"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "reversible defect"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "<=120 mg/dl"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", ">120 mg/dl"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient ID:</span></p></body></html>"))






# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================

# Form implementation generated from reading ui file 'finalgui/final5.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
window_width = 1105
window_height = 902
class final5_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 902)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 271, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 500, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 371, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 500, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 500, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 400, 500, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 460, 511, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 520, 500, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 580, 721, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(850, 40, 171, 22))
        self.lineEdit.setStyleSheet("background-color:#fff;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(850, 100, 171, 22))
        self.comboBox.setStyleSheet("background-color:#fff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(850, 160, 171, 22))
        self.comboBox_2.setStyleSheet("background-color:#fff;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(350, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 40, 371, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(850, 220, 171, 22))
        self.lineEdit_6.setStyleSheet("background-color:#fff;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(850, 280, 171, 22))
        self.lineEdit_7.setStyleSheet("background-color:#fff;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(850, 340, 171, 22))
        self.comboBox_10.setStyleSheet("background-color:#fff;")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_11.setGeometry(QtCore.QRect(850, 400, 171, 22))
        self.comboBox_11.setStyleSheet("background-color:#fff;")
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(850, 460, 171, 22))
        self.lineEdit_8.setStyleSheet("background-color:#fff;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox_12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_12.setGeometry(QtCore.QRect(850, 520, 171, 22))
        self.comboBox_12.setStyleSheet("background-color:#fff;")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(850, 580, 171, 22))
        self.lineEdit_9.setStyleSheet("background-color:#fff;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 640, 721, 31))
        self.label_11.setObjectName("label_11")
        self.comboBox_13 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_13.setGeometry(QtCore.QRect(850, 640, 171, 22))
        self.comboBox_13.setStyleSheet("background-color:#fff;")
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 700, 721, 31))
        self.label_12.setObjectName("label_12")
        self.comboBox_14 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_14.setGeometry(QtCore.QRect(850, 700, 171, 22))
        self.comboBox_14.setStyleSheet("background-color:#fff;")
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 760, 721, 31))
        self.label_13.setObjectName("label_13")
        self.comboBox_15 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_15.setGeometry(QtCore.QRect(850, 760, 171, 22))
        self.comboBox_15.setStyleSheet("background-color:#fff;")
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 820, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient Gender:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient restbp(resting blood pressure):</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient cp(chest pain): </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient chol(serum cholestrol level):</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient fbs(fasting blood sugar): </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient restecg (resting electrocardiography):</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient thalach (maximum heart rate achieved):</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient exang (exercise induced angina):</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient oldpeak (ST depression induced by exercise relative to rest):</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Typical Angina"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Atypical Angina"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Non Angina"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Asymptomatic Angina"))
        self.label_15.setText(_translate("MainWindow", "Enter the details given below:"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient Age:</span></p></body></html>"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "<=120 mg/dl"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", ">120 mg/dl"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "normal"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "ST-T wave abnormality"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "left ventricular hypertrophy"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "No"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient slope (slope of peak exercise ST segment):</span></p></body></html>"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "upsloping"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "flat"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "downsloping"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient ca (number of major vessels colored by fluoroscopy):</span></p></body></html>"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "3"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter patient thal( thalassemia):</span></p></body></html>"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "normal"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "fixed defect"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "reversible defect"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))





# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================================================================================================================================================================================================================================

import pandas as pd

# Importing the dataset

dataset = pd.read_csv('HealthData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 13].values

# handling missing data

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 11:13])
X[:, 11:13] = imputer.transform(X[:, 11:13])

# splitting dataset into training set and test set

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25)

# feature scaling

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

####------------similarly can be seen for all the attributes------------------

#### logistic regression

# fitting LR to training set

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

# Predict the test set results

y_Class_pred = classifier.predict(X_test)

# checking the accuracy for predicted results

from sklearn.metrics import accuracy_score

accuracy_score(Y_test, y_Class_pred)

# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test, y_Class_pred)
print(cm)

# Interpretation:

from sklearn.metrics import classification_report

print(classification_report(Y_test, y_Class_pred))



a = "global"
class MainPage1(final1_Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage1, self).__init__()
        loadUi("final1.ui", self)
        self.pushButton.clicked.connect(self.start_now)

    #this will take you to next window
    def start_now(self):
        self.main = MainPage2()
        w.hide()
        self.main.show()


class MainPage2(final2_Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage2,self).__init__()
        loadUi("final2.ui",self)
        self.pushButton.clicked.connect(self.new_user)
        self.pushButton_2.clicked.connect(self.update_user)

    # this will take you to next window
    def new_user(self):
        self.main = MainPage3()
        self.main.show()


    def update_user(self):
        self.main = MainPage4()
        self.main.show()

class MainPage3(final3_Ui_MainWindow,QtWidgets.QMainWindow):
    row = []
    def __init__(self):
        super(MainPage3,self).__init__()
        loadUi("final3.ui",self)
        self.pushButton.clicked.connect(self.user_details)

    def user_details(self):
        name = self.lineEdit.text()
        age = self.lineEdit_2.text()
        gender = self.comboBox.currentText()
        mobile = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        address = self.lineEdit_5.text()

        # Table 1
        con = sqlite3.connect('data.db')
        cursor = con.cursor()

        con.execute("""Create table IF NOT EXISTS PATIENT
                           (PATIENT_ID integer PRIMARY KEY AUTOINCREMENT,
                            NAME VARCHAR(20) not null,
                            AGE INTEGER not null,
                            GENDER varchar(10) not null,
                            MOBILE_NO INTEGER(10) not null,
                            EMAIL varchar(20) not null,
                            ADDRESS varcahr(100) not null
                            )""")

        cursor.execute("""INSERT INTO PATIENT(
                            NAME,
                            AGE,
                            GENDER,
                            MOBILE_NO,
                            EMAIL,
                            ADDRESS
                            )

                        VALUES
                        (?,?,?,?,?,?)
                        """, (name,age,gender,mobile,email,address))

        con.commit()
        global a
        for a in cursor.execute("""SELECT PATIENT_ID FROM PATIENT WHERE name = ? AND MOBILE_NO = ? AND EMAIL = ?;""",(name,mobile,email)):
            pop_message(text="Your Id is: '{}'".format(a[0]))

        self.main = MainPage5()
        self.main.show()


class MainPage4(final4_Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage4,self).__init__()
        loadUi("final4.ui",self)
        self.pushButton.clicked.connect(self.update_details)


    def update_details(self):
        p_id2 = self.lineEdit_2.text()
        age = self.lineEdit.text()
        gender = self.comboBox.currentText()
        if gender == 'Male':
            gender = 1
        elif gender == 'Female':
            gender = 0
        else:
            return None

        chest_pain = self.comboBox_2.currentText()
        if chest_pain == 'Typical Angina':
            chest_pain = 1
        elif chest_pain == 'Atypical Angina':
            chest_pain = 2
        elif chest_pain == 'Non Angina':
            chest_pain = 3
        elif chest_pain == 'Asymptomatic Angina':
            chest_pain = 4
        else:
            chest_pain = None


        blood_pressure = self.lineEdit_6.text()
        cholestrol = self.lineEdit_7.text()

        blood_sugar = self.comboBox_10.currentText()
        if blood_sugar == '<=120 mg/dl':
            blood_sugar = 0
        elif blood_sugar == '>120 mg/dl':
            blood_sugar = 1
        else:
            blood_sugar = None

        restecg = self.comboBox_11.currentText()
        if restecg == 'normal':
            restecg = 0
        elif restecg == 'ST-T wave abnormality':
            restecg = 1
        elif restecg == 'left ventricular hypertrophy':
            restecg = 2
        else:
            restecg = None

        heart_rate = self.lineEdit_8.text()
        exercise_angina = self.comboBox_12.currentText()
        if exercise_angina == 'No':
            exercise_angina = 0
        elif exercise_angina == 'Yes':
            exercise_angina = 1
        else:
            exercise_angina = None


        depression = self.lineEdit_9.text()
        slope = self.comboBox_13.currentText()
        if slope == 'upsloping':
            slope = 1
        elif slope == 'flat':
            slope = 2
        elif slope == 'downsloping':
            slope = 3
        else:
            slope = None

        vessels = self.comboBox_14.currentText()
        thalassemia = self.comboBox_15.currentText()
        if thalassemia == 'normal':
            thalassemia = 3
        elif thalassemia == 'fixed defect':
            thalassemia = 6
        elif thalassemia == 'reversible defect':
            thalassemia = 7
        else:
            thalassemia = None

        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        print("db")

        # Update Table
        sql = "update PATIENT_COLUMNS set Age = '{}',Sex = '{}',chest_pain = '{}',blood_pressure='{}',cholestrol='{}',blood_sugar='{}',restecg='{}',heart_rate='{}',exercise_angina='{}',depression='{}',slope='{}',vessels='{}',thalassemia='{}' where Id='{}'".format(
            age, gender, chest_pain, blood_pressure, cholestrol, blood_sugar, restecg, heart_rate, exercise_angina, depression, slope, vessels, thalassemia,
            p_id2)
        cursor.execute(sql)

        # Convert to csv file
        # 1. Create SQL Statement
        sql = "select age, Sex, chest_pain, blood_pressure, cholestrol, blood_sugar, restecg, heart_rate, exercise_angina, depression, slope, vessels, thalassemia from PATIENT_COLUMNS where Id ={} ".format(p_id2)
        # print(sql)

        # 2. Create Connection with Database
        # 3. Obtain Cursor to execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        import csv
        row = list(cursor.fetchone())
        r = "".join(repr(e) for e in row)
        with open("Testing_data.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerow(row)

        con.commit()
        print("User Columns Updated!!")
        cursor.close()
        con.close()

        Newdataset = pd.read_csv('Testing_data.csv')
        ynew = classifier.predict(Newdataset)

        if ynew[0] == 0:
            self.print_prediction = 0
            print('Healthy')
            healthy_msg()

        elif ynew[0] == 1:
            self.print_prediction = 1
            print('Not Healthy')
            risk_msg()

        sys.exit()

class MainPage5(final5_Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MainPage5,self).__init__()
        loadUi("final5.ui",self)
        self.pushButton.clicked.connect(self.user_columns)


    def user_columns(self):

        age = self.lineEdit.text()
        gender = self.comboBox.currentText()
        if gender == 'Male':
            gender = 1
        elif gender == 'Female':
            gender = 0
        else:
            return None

        chest_pain = self.comboBox_2.currentText()
        if chest_pain == 'Typical Angina':
            chest_pain = 1
        elif chest_pain == 'Atypical Angina':
            chest_pain = 2
        elif chest_pain == 'Non Angina':
            chest_pain = 3
        elif chest_pain == 'Asymptomatic Angina':
            chest_pain = 4
        else:
            chest_pain = None

        blood_pressure = self.lineEdit_6.text()
        cholestrol = self.lineEdit_7.text()

        blood_sugar = self.comboBox_10.currentText()
        if blood_sugar == '<=120 mg/dl':
            blood_sugar = 0
        elif blood_sugar == '>120 mg/dl':
            blood_sugar = 1
        else:
            blood_sugar = None

        restecg = self.comboBox_11.currentText()
        if restecg == 'normal':
            restecg = 0
        elif restecg == 'ST-T wave abnormality':
            restecg = 1
        elif restecg  == 'left ventricular hypertrophy':
            restecg = 2
        else:
            restecg = None

        heart_rate = self.lineEdit_8.text()
        exercise_angina = self.comboBox_12.currentText()
        if exercise_angina == 'No':
            exercise_angina = 0
        elif exercise_angina == 'Yes':
            exercise_angina = 1
        else:
            exercise_angina = None


        depression = self.lineEdit_9.text()
        slope = self.comboBox_13.currentText()
        if slope == 'upsloping':
            slope = 1
        elif slope == 'flat':
            slope = 2
        elif slope  == 'downsloping':
            slope = 3
        else:
            slope = None

        vessels = self.comboBox_14.currentText()
        thalassemia = self.comboBox_15.currentText()
        if thalassemia == 'normal':
            thalassemia = 3
        elif thalassemia == 'fixed defect':
            thalassemia = 6
        elif thalassemia  == 'reversible defect':
            thalassemia = 7
        else:
            thalassemia = None


        global a

        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        print("db")

        # Table 2
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS PATIENT_COLUMNS(Id integer PRIMARY KEY,
                                                Age integer ,
                                                Sex integer,
                                                chest_pain integer,
                                                blood_pressure integer,
                                                cholestrol integer,
                                                blood_sugar integer,
                                                restecg integer,
                                                heart_rate integer,
                                                exercise_angina integer,
                                                depression integer,
                                                slope integer,
                                                vessels integer,
                                                thalassemia integer)""")

        cursor.execute("""INSERT INTO PATIENT_COLUMNS(
                            Age,
                            Sex,
                            chest_pain,
                            blood_pressure,
                            cholestrol,
                            blood_sugar,
                            restecg,
                            heart_rate,
                            exercise_angina,
                            depression,
                            slope,
                            vessels,
                            thalassemia)

                        VALUES
                        (?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """, (age, gender, chest_pain, blood_pressure, cholestrol, blood_sugar, restecg, heart_rate, exercise_angina, depression, slope, vessels, thalassemia))

        # Convert to csv file
        # 1. Create SQL Statement
        sql = "select age, Sex, chest_pain, blood_pressure, cholestrol, blood_sugar, restecg, heart_rate, exercise_angina, depression, slope, vessels, thalassemia from PATIENT_COLUMNS where Id ={} ".format(a[0])
        print(sql)

        # 2. Create Connection with Database
        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        import csv
        row = list(cursor.fetchone())
        r = "".join(repr(e) for e in row)
        with open("Testing_data.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerow(row)


        con.commit()

        print("User Columns Saved!!")
        cursor.close()
        con.close()


        Newdataset = pd.read_csv('Testing_data.csv')
        ynew = classifier.predict(Newdataset)


        if ynew[0] == 0:
            self.print_prediction = 0
            print('Healthy')
            healthy_msg()

        elif ynew[0] == 1:
            self.print_prediction = 1
            print('Not Healthy')
            risk_msg()

        sys.exit()


def pop_message(text=""):
    msg = QMessageBox()
    msg.setText("{}".format(text))
    msg.exec_()


def healthy_msg():
    msg_good = QMessageBox()
    msg_good.setWindowTitle('Prediction Result')
    msg_good.setText('You does not have Heart Disease.')
    msg_good.setIcon(QMessageBox.Information)
    msg_good.setGeometry(700 + (window_width // 9), 50 + (window_height // 2), 50, 50)
    msg_good.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_good.exec_()


def risk_msg():
    msg_bad = QMessageBox()
    msg_bad.setWindowTitle('Prediction Result')
    msg_bad.setIcon(QMessageBox.Critical)
    msg_bad.setText('You have Heart Disease. Consult Doctor.')
    msg_bad.setGeometry(700 + (window_width // 9), 50 + (window_height // 2), 50, 50)
    msg_bad.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_bad.exec_()





app = QApplication(sys.argv)
w = MainPage1()
w.show()
sys.exit(app.exec_())



# Form implementation generated from reading ui file 'entry_exit.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 433)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 191, 41))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 100, 131, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 150, 131, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 271, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.SecondName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SecondName.setGeometry(QtCore.QRect(130, 110, 421, 31))
        self.SecondName.setObjectName("SecondName")
        self.Name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(130, 160, 421, 31))
        self.Name.setObjectName("Name")
        self.ID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(310, 210, 241, 31))
        self.ID.setObjectName("ID")
        self.Error2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error2.setGeometry(QtCore.QRect(270, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Error2.setFont(font)
        self.Error2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Error2.setObjectName("Error2")
        self.Error3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error3.setGeometry(QtCore.QRect(270, 140, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Error3.setFont(font)
        self.Error3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Error3.setObjectName("Error3")
        self.Error4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error4.setGeometry(QtCore.QRect(270, 190, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Error4.setFont(font)
        self.Error4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Error4.setObjectName("Error4")
        self.Confirm = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.Confirm.setGeometry(QtCore.QRect(40, 310, 381, 51))
        self.Confirm.setObjectName("Confirm")
        self.Submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(220, 360, 151, 51))
        self.Submit.setObjectName("Submit")
        self.IfEntry = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.IfEntry.setGeometry(QtCore.QRect(50, 260, 61, 41))
        self.IfEntry.setObjectName("IfEntry")
        self.IfExit = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.IfExit.setGeometry(QtCore.QRect(130, 260, 81, 41))
        self.IfExit.setObjectName("IfExit")
        self.PlacesLeft = QtWidgets.QLabel(parent=self.centralwidget)
        self.PlacesLeft.setGeometry(QtCore.QRect(230, 250, 251, 41))
        self.PlacesLeft.setObjectName("PlacesLeft")
        self.IfParking = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.IfParking.setGeometry(QtCore.QRect(230, 280, 251, 41))
        self.IfParking.setObjectName("IfParking")
        self.IfGuest = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.IfGuest.setGeometry(QtCore.QRect(60, 60, 61, 41))
        self.IfGuest.setObjectName("IfGuest")
        self.GuestTime = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.GuestTime.setGeometry(QtCore.QRect(130, 70, 113, 31))
        self.GuestTime.setObjectName("GuestTime")
        self.Error1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Error1.setGeometry(QtCore.QRect(-40, 40, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Error1.setFont(font)
        self.Error1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Error1.setObjectName("Error1")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-40, 50, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Запись входа/выхода"))
        self.label_2.setText(_translate("MainWindow", "Фамилия:"))
        self.label_3.setText(_translate("MainWindow", "Имя:"))
        self.label_4.setText(_translate("MainWindow", "Номер индивидуального пропуска:"))
        self.Error2.setText(_translate("MainWindow", "*Поле не заполнено/ заполнено неправильно"))
        self.Error3.setText(_translate("MainWindow", "*Поле не заполнено/ заполнено неправильно"))
        self.Error4.setText(_translate("MainWindow", "*Поле не заполнено/ заполнено неправильно"))
        self.Confirm.setText(_translate("MainWindow", "Подтверждаю правильность введенных данных"))
        self.Submit.setText(_translate("MainWindow", "Подтвердить"))
        self.IfEntry.setText(_translate("MainWindow", "Вход"))
        self.IfExit.setText(_translate("MainWindow", "Выход"))
        self.PlacesLeft.setText(_translate("MainWindow", "Парковочных мест доступно: 10"))
        self.IfParking.setText(_translate("MainWindow", "Выписать парковочный талон"))
        self.IfGuest.setText(_translate("MainWindow", "Гость"))
        self.Error1.setText(_translate("MainWindow", "*Поле не заполнено/ заполнено неправильно"))
        self.label_10.setText(_translate("MainWindow", "Время действия пропуска(в часах)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

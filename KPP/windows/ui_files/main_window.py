# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 697)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.History = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.History.setGeometry(QtCore.QRect(30, 180, 481, 211))
        self.History.setObjectName("History")
        self.Parking = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.Parking.setGeometry(QtCore.QRect(530, 180, 301, 211))
        self.Parking.setObjectName("Parking")
        self.ExitEntryBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ExitEntryBtn.setGeometry(QtCore.QRect(30, 80, 181, 51))
        self.ExitEntryBtn.setObjectName("ExitEntryBtn")
        self.Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(30, 30, 411, 41))
        self.Label.setObjectName("Label")
        self.NewEmployeeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.NewEmployeeBtn.setGeometry(QtCore.QRect(220, 80, 281, 51))
        self.NewEmployeeBtn.setObjectName("NewEmployeeBtn")
        self.GuestsList = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.GuestsList.setGeometry(QtCore.QRect(30, 440, 481, 221))
        self.GuestsList.setObjectName("GuestsList")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 231, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 410, 151, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 150, 211, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 410, 211, 21))
        self.label_5.setObjectName("label_5")
        self.EmployeeList = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.EmployeeList.setGeometry(QtCore.QRect(530, 440, 301, 221))
        self.EmployeeList.setObjectName("EmployeeList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExitEntryBtn.setText(_translate("MainWindow", "Записать вход/выход"))
        self.Label.setText(_translate("MainWindow", "Система управления контрольно пропускного пункта"))
        self.NewEmployeeBtn.setText(_translate("MainWindow", "Записать нового сотрудника"))
        self.label_2.setText(_translate("MainWindow", "История входов и выходов:"))
        self.label_3.setText(_translate("MainWindow", "Гости:"))
        self.label_4.setText(_translate("MainWindow", "Парковочные места:"))
        self.label_5.setText(_translate("MainWindow", "Сотрудники:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

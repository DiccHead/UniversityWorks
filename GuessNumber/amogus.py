from PyQt6 import QtCore, QtGui, QtWidgets

font = QtGui.QFont()
font.setPointSize(12)
centralwidget = QtWidgets.QWidget()
centralwidget.setFont(font)
centralwidget.setObjectName("centralwidget")
label = QtWidgets.QLabel(parent=centralwidget)
label.setGeometry(QtCore.QRect(260, 90, 271, 91))
font = QtGui.QFont()
font.setPointSize(26)
label.setFont(font)
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setObjectName("label")
label_2 = QtWidgets.QLabel(parent=centralwidget)
label_2.setGeometry(QtCore.QRect(80, 280, 171, 31))
label_2.setObjectName("label_2")
label_3 = QtWidgets.QLabel(parent=centralwidget)
label_3.setGeometry(QtCore.QRect(420, 280, 181, 31))
label_3.setObjectName("label_3")
label_4 = QtWidgets.QLabel(parent=centralwidget)
label_4.setGeometry(QtCore.QRect(290, 380, 171, 31))
label_4.setObjectName("label_4")
lineEdit = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit.setGeometry(QtCore.QRect(240, 280, 113, 31))
lineEdit.setObjectName("lineEdit")
lineEdit_2 = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit_2.setGeometry(QtCore.QRect(590, 280, 113, 31))
lineEdit_2.setObjectName("lineEdit_2")
lineEdit_3 = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit_3.setGeometry(QtCore.QRect(470, 380, 113, 31))
lineEdit_3.setObjectName("lineEdit_3")
pushButton = QtWidgets.QPushButton(parent=centralwidget)
pushButton.setGeometry(QtCore.QRect(320, 430, 161, 41))
pushButton.setObjectName("pushButton")

label.setText("Угадай число!")
label_2.setText("Минимальное число:")
label_3.setText("Максимальное число:")
label_4.setText("Колличество попытов:")
lineEdit.setText("1")
lineEdit_2.setText("100")
lineEdit_3.setText("10")
pushButton.setText("Начать")
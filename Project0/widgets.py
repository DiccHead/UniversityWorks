from PyQt6 import QtWidgets, QtGui, QtCore


Window1 = QtWidgets.QWidget()
Window1.setObjectName("Window1")
label = QtWidgets.QLabel(parent=Window1)
label.setGeometry(QtCore.QRect(250, 90, 331, 131))
font = QtGui.QFont()
font.setPointSize(26)
label.setFont(font)
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setObjectName("label")
label_2 = QtWidgets.QLabel(parent=Window1)
label_2.setGeometry(QtCore.QRect(70, 290, 161, 20))
font = QtGui.QFont()
font.setPointSize(12)
label_2.setFont(font)
label_2.setObjectName("label_2")
label_3 = QtWidgets.QLabel(parent=Window1)
label_3.setGeometry(QtCore.QRect(190, 390, 181, 21))
font = QtGui.QFont()
font.setPointSize(12)
label_3.setFont(font)
label_3.setObjectName("label_3")
label_4 = QtWidgets.QLabel(parent=Window1)
label_4.setGeometry(QtCore.QRect(420, 290, 171, 20))
font = QtGui.QFont()
font.setPointSize(12)
label_4.setFont(font)
label_4.setObjectName("label_4")
lineEdit = QtWidgets.QLineEdit(parent=Window1)
lineEdit.setGeometry(QtCore.QRect(250, 280, 151, 41))
font = QtGui.QFont()
font.setPointSize(12)
lineEdit.setFont(font)
lineEdit.setObjectName("lineEdit")
lineEdit_2 = QtWidgets.QLineEdit(parent=Window1)
lineEdit_2.setGeometry(QtCore.QRect(590, 280, 161, 41))
font = QtGui.QFont()
font.setPointSize(12)
lineEdit_2.setFont(font)
lineEdit_2.setObjectName("lineEdit_2")
lineEdit_3 = QtWidgets.QLineEdit(parent=Window1)
lineEdit_3.setGeometry(QtCore.QRect(380, 380, 161, 41))
font = QtGui.QFont()
font.setPointSize(12)
lineEdit_3.setFont(font)
lineEdit_3.setObjectName("lineEdit_3")
pushButton = QtWidgets.QPushButton(parent=Window1)
pushButton.setGeometry(QtCore.QRect(310, 460, 151, 31))
font = QtGui.QFont()
font.setPointSize(14)
pushButton.setFont(font)
pushButton.setObjectName("pushButton")
label.setText("Угадай число")
label_2.setText("Минимальное число:")
label_3.setText("Колличество попыток:")
label_4.setText("Максимальное число:")
lineEdit.setText("1")
lineEdit_2.setText("100")
lineEdit_3.setText("10")
pushButton.setText("Начать!")

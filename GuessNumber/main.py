from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys, random

stacked = 0
min_num = 1
max_num = 100
attempts = 10
correct = 0

def main():
    app = QApplication(sys.argv)
    import amogus, amogus2

    global stacked
    win = QMainWindow()
    stacked = QStackedWidget()
    stacked.addWidget(amogus.centralwidget)
    stacked.addWidget(amogus2.centralwidget)
    stacked.setCurrentWidget(amogus.centralwidget)
    win.resize(800, 600)
    win.setCentralWidget(stacked)

    amogus.pushButton.clicked.connect(setWin2)
    amogus2.pushButton_2.clicked.connect(setWin1)
    amogus2.pushButton_3.clicked.connect(app.quit)
    amogus2.pushButton.clicked.connect(enter)

    win.show()
    sys.exit(app.exec())


def setWin2():
    import amogus, amogus2
    global stacked, min_num, max_num, attempts, correct
    min_num = int(amogus.lineEdit.text())
    max_num = int(amogus.lineEdit_2.text())
    attempts = int(amogus.lineEdit_3.text())
    stacked.setCurrentWidget(amogus2.centralwidget)
    amogus2.label_2.setText("Осталось попыток: " + str(attempts))
    amogus2.lineEdit.setText("")
    correct = random.randint(min_num, max_num)
    amogus2.pushButton.setDisabled(False)


def setWin1():
    import amogus, amogus2
    global stacked
    stacked.setCurrentWidget(amogus.centralwidget)


def enter():
    import amogus2
    global attempts
    user_input = int(amogus2.lineEdit.text())
    if user_input < correct:
        attempts -= 1
        amogus2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ больше.")
        amogus2.lineEdit.setText("")
    if user_input > correct:
        attempts -= 1
        amogus2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ меньше.")
        amogus2.lineEdit.setText("")
    if attempts == 0 and user_input != correct:
        amogus2.label_2.setText(f"Неправильно, ответ был {correct}!")
        amogus2.pushButton.setDisabled(True)
    if user_input == correct:
        amogus2.label_2.setText("Вы угадали!")

if __name__ == "__main__":
    main()
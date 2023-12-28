from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys, random

stacked = 0
min_num = 1
max_num = 100
attempts = 10
correct = 0

def main():
    app = QApplication(sys.argv)
    import widgets, widgets2

    global stacked
    win = QMainWindow()
    stacked = QStackedWidget()
    stacked.addWidget(widgets.Window1)
    stacked.addWidget(widgets2.Window2)
    stacked.setCurrentWidget(widgets.Window1)
    win.resize(800, 600)
    win.setCentralWidget(stacked)
    #Connecting signals
    widgets.pushButton.clicked.connect(setWin2)
    widgets2.pushButton_3.clicked.connect(app.quit)
    widgets2.pushButton_2.clicked.connect(setWin1)
    widgets2.pushButton.clicked.connect(enter)

    win.show()
    sys.exit(app.exec())


def setWin2():
    import widgets2, widgets
    global stacked, min_num, max_num, attempts, correct
    min_num = int(widgets.lineEdit.text())
    max_num = int(widgets.lineEdit_2.text())
    attempts = int(widgets.lineEdit_3.text())
    stacked.setCurrentWidget(widgets2.Window2)
    widgets2.label_2.setText("Осталось попыток: " + str(attempts))
    widgets2.lineEdit.setText("")
    widgets2.pushButton.setDisabled(False)
    correct = random.randint(min_num, max_num)


def setWin1():
    import widgets
    global stacked, min_num, max_num, attempts
    stacked.setCurrentWidget(widgets.Window1)


def enter():
    import widgets2
    global attempts
    user_input = int(widgets2.lineEdit.text())
    if user_input < correct:
        attempts -= 1
        widgets2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ больше.")
        widgets2.lineEdit.setText("")
    if user_input > correct:
        attempts -= 1
        widgets2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ меньше.")
        widgets2.lineEdit.setText("")
    if attempts == 0 and user_input != correct:
        widgets2.label_2.setText(f"Неправильно, ответ был {correct}!")
        widgets2.pushButton.setDisabled(True)
    if user_input == correct:
        widgets2.label_2.setText("Вы угадали!")




if __name__ == "__main__":
    main()
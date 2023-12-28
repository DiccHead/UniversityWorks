import random, sys
from PyQt6.QtWidgets import QApplication, QMainWindow



def main():
    app = QApplication(sys.argv)
    import bonewidgets

    win = QMainWindow()
    win.resize(800, 600)
    win.setCentralWidget(bonewidgets.centralwidget)

    bonewidgets.pushButton.clicked.connect(enter)

    win.show()
    sys.exit(app.exec())

def enter():
    import bonewidgets
    iterlist = []
    stats = []
    fullnum = 0
    iternum = int(bonewidgets.lineEdit.text())

    for i in range(iternum+1):
        iterlist.append(random.randint(1, 6))

    for j in range(1, 7):
        fullnum += iterlist.count(j)/iternum
        stats.append(iterlist.count(j)/iternum)
    
    bonewidgets.label_9.setText(str(stats[0]))
    bonewidgets.label_10.setText(str(stats[1]))
    bonewidgets.label_11.setText(str(stats[2]))
    bonewidgets.label_12.setText(str(stats[3]))
    bonewidgets.label_13.setText(str(stats[4]))
    bonewidgets.label_14.setText(str(stats[5]))

    

if __name__ == "__main__":
    main()
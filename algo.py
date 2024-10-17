from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QHBoxLayout, QVBoxLayout

app = QApplication([])

my_win = QWidget()

my_win.setWindowTitle('My first App')
my_win.move(900,400)
my_win.resize(700,400)


layout1 = QVBoxLayout()

label1 = QLabel('Hello Guys!')
label2 = QLabel('My name is Revan')
layout1.addWidget(label1,alignment=Qt.AlignCenter)
layout1.addWidget(label2,alignment=Qt.AlignCenter)


my_win.setLayout(layout1)
my_win.show()

app.exec_()


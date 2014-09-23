#!/usr/bin/python3.4

from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets

from forms.c_gui import MainForm

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec()

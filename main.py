
import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow


from Home.View.homeView import Ui_Form

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())




import sys
import Home.View.home_rc


from PyQt5.QtWidgets import QApplication, QMainWindow

#from Home.View.homeView import Ui_Form
from Login.View.loginView import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



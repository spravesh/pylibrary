import sys

from PyQt5.Qt import QWidget, QApplication

from main.DeleteBookUI import DeleteBookUI


class LibrarianPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Admin Panel"
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.next=DeleteBookUI()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    


app = QApplication(sys.argv)
ex = LibrarianPanel()
sys.exit(app.exec_())
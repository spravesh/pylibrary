import sys

from PyQt5.Qt import QWidget, QApplication, QPushButton

from main.AddBookUI import AddBookUI
from main.EditBookUI import EditBookUI
from main.DeleteBookUI import DeleteBookUI
from main.AddUserUI import AddUserUI
from main.EditUser import EditUserUI
from main.DeleteUserUI import DeleteUserUI

class AdminPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Admin Panel"
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.addUserUI=AddUserUI()
        self.editUserUI=EditUserUI()
        self.deleteUserUI=DeleteUserUI()
        self.addBookUI=AddBookUI()
        self.editBookUI=EditBookUI()
        self.deleteBookUI=DeleteBookUI()
        self.initUI()
        
    def initUI(self):
        self.addUser=QPushButton("Add Users",self)
        self.addUser.move(100,100)
        self.addUser.clicked.connect(self.onadduser)
        self.editUser=QPushButton("Edit Users",self)
        self.editUser.move(100,130)
        #self.editUser.clicked.connect(self.EditUserUIStart)
        self.deleteUser=QPushButton("Delete Users",self)
        #self.deleteUser.clicked.connect(self.onclick)
        self.deleteUser.move(100,160)
        self.addBook=QPushButton("Add Books",self)
        #self.addBook.clicked.connect(self.onclick)
        self.addBook.move(100,190)
        self.editBook=QPushButton("Edit Books",self)
        #self.editBook.clicked.connect(self.onclick)
        self.editBook.move(100,220)
        self.deleteBook=QPushButton("Delete Book",self)
        self.deleteBook.move(100,250)
        #self.deleteBook.clicked.connect(self.onclick)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
    def onadduser(self):
        self.addUserUI.show()
        

'''
Created on Jun 18, 2018

@author: Pravesh
'''
'''
Created on Jun 18, 2018

@author: Pravesh
'''
import sys
from PyQt5.Qt import QLineEdit, QLabel, QComboBox, QPushButton, QStatusBar
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from config import Base,create_engine,Session
from tables import User
session = Session()


class AddUserUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.initUI()
        
    def initUI(self):
        self.labelUsername = QLabel(self)
        self.labelUsername.setText("Username")
        self.labelPassword = QLabel(self)
        self.labelPassword.setText("Password")
        self.labelRole = QLabel(self)
        self.labelRole.setText("Role")
        self.labelUsername.move(250, 100)
        self.labelPassword.move(250, 130)
        self.labelRole.move(250, 160)
        self.username = QLineEdit(self)
        self.username.move(300, 100)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(300, 130)
        self.role = QComboBox(self)
        self.role.addItem("Student")
        self.role.addItem("Librarian")
        self.role.addItem("Admin")
        self.role.move(300, 160)
        
        button = QPushButton("Add User", self)
        button.move(300, 190)
        button.clicked.connect(self.add_user)
       
        self.setWindowTitle("Add Users")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
    def add_user(self):
        uname = self.username.text();
        password = self.password.text();
        role = self.role.currentText()
        print(uname)
        print(password)
        print(role)
        user = User(uname, password, role)
        session.add(user)
        session.commit()
        self.statusBar().showMessage("User Saved Successfully")
            
        
app = QApplication(sys.argv)
ex = AddUserUI()
sys.exit(app.exec_())


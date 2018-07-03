import sys

from PyQt5.Qt import QWidget, QApplication, QLabel, QLineEdit, QPushButton

from main.DeleteBookUI import DeleteBookUI
from config import Session
from tables import User
from main.AdminPanel import AdminPanel

class Login(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title="Admin Panel"
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.adminPanelUI=AdminPanel()
        self.initUI()
        
    def initUI(self):
        self.lblusername=QLabel(self)
        self.lblpassword=QLabel(self)
        self.lblusername.move(200,100)
        self.lblusername.setText("USERNAME")
        self.lblpassword.move(200,140)
        self.lblpassword.setText("PASSWORD")
        self.username=QLineEdit(self)
        self.username.move(250,100)
        
        self.password=QLineEdit(self)
        self.password.move(250,140)
        self.password.setEchoMode(QLineEdit.Password)
        
        
        self.login=QPushButton("Login",self)
        self.login.move(280,300)
        
        self.login.clicked.connect(self.onclick)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    

    def onclick(self):
        user=self.session.query(User).filter(User.username==self.username.text()).first()
        print("User Exists")
        if(user.password==self.password.text()):
                role=user.role
                print(role)
                if(role=="Student"):
                    print("It is a student")
                elif(role=="Librarian"):
                    print("Redirect to the librarian UI")
                else:
                    self.adminPanelUI.show()
                    
            
        
    
        
        
app = QApplication(sys.argv)
ex = Login()
sys.exit(app.exec_())
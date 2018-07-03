import sys

from PyQt5.Qt import QWidget, QApplication, QLabel, QComboBox, QPushButton

from main.DeleteBookUI import DeleteBookUI
from tables import User,Book,Issue
from config import Session

class IssueBook(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title="Admin Panel"
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.initUI()
        
    def initUI(self):
        
        self.lblIssuedTo=QLabel(self)
        self.lblIssuedTo.setText("Issued To")
        self.lblIssuedTo.move(180,100)
        
        self.lblBook=QLabel(self)
        self.lblBook.setText("Book")
        self.lblBook.move(180,130)
        
        self.issuedTo=QComboBox(self)
        self.issuedTo.move(220,100)
        self.populateUsers(self.issuedTo)
        
        self.Book=QComboBox(self)
        self.Book.move(220,130)
        self.populateBooks(self.Book)
        
        
        self.saveBtn=QPushButton("Issue Book",self)
        self.saveBtn.move(250,200)
        self.saveBtn.clicked.connect(self.saveIssue)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    

    def populateUsers(self,combobox):
        users=self.session.query(User).filter(User.role=="Student")
        for user in users:
            combobox.addItem(user.username)
        
    def populateBooks(self,combobox):
        books=self.session.query(Book).all()
        for book in books:
            combobox.addItem(book.name)
    
    def saveIssue(self):
        issued_to=self.session.query(User).filter(User.username==self.issuedTo.currentText()).first()
        book=self.session.query(Book).filter(Book.name==self.Book.currentText()).first()
        try:
            issued=Issue(issued_to.id,book.id)
            self.session.add(issued)
            self.session.commit()
        except:
            print("An error occured")
        
app = QApplication(sys.argv)
ex = IssueBook()
sys.exit(app.exec_())
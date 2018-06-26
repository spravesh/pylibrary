import sys
    
from PyQt5.Qt import QLineEdit, QLabel, QComboBox, QPushButton, QStatusBar
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from config import  Base, Session, engine
from tables import  Book
session = Session()
    
class AddBookUI(QMainWindow):
    
    def __init__(self):
            super().__init__()                          
            self.width = 640
            self.height = 400
            self.top = 500
            self.left = 400
            self.initUI()
            
    def initUI(self):
            self.labelBookName = QLabel(self)
            self.labelBookName.setText("Book Name")
            self.labelAuthor = QLabel(self)
            self.labelAuthor.setText("Author")
            self.labelBookName.move(250, 100)
            self.labelAuthor.move(250, 130)
            
            self.bookname = QLineEdit(self)
            self.bookname.move(300, 100)
            self.author = QLineEdit(self)
            self.author.move(300, 130)
            button = QPushButton("Add Book", self)
            button.move(300, 190)
            button.clicked.connect(self.add_book)
           
            self.setWindowTitle("Add Books")
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show()
            
    def add_book(self):
            book = self.bookname.text();
            author = self.author.text();
            print(book)
            print(author)
            book = Book(book, author)
            session.add(book)
            session.commit()
            self.statusBar().showMessage("Book Saved Successfully")
            self.bookname.clear()
            self.author.clear()
            
app = QApplication(sys.argv)
ex = AddBookUI()
sys.exit(app.exec_())
    

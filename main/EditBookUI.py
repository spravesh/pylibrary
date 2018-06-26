import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLineEdit, QLabel, QComboBox, QPushButton, QStatusBar
from PyQt5.QtCore import pyqtSlot
from config import Session 
from tables import Book


class editpopup(QWidget):
    book_id=""
    session=Session()
    def __init__(self):
        super().__init__()
        self.title="Edit Pop Up"
        self.width = 500
        self.height = 500
        self.top = 100
        self.left = 100
        self.initUI()
    def initUI(self):
        self.bookname=QLineEdit(self)
        self.bookname.move(200,200)
        
        self.author=QLineEdit(self)
        self.author.move(200,240)
        
        self.savechanges=QPushButton("Save changes",self)
        self.savechanges.move(250,300)
        self.savechanges.clicked.connect(self.updateValues)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
    def setValues(self,book_id,book_name,book_author):
           self.book_id=book_id
           self.bookname.setText(book_name)
           self.author.setText(book_author)
           
    def updateValues(self):
        result=self.session.query(Book).filter(Book.id==self.book_id).first()
        result.name=self.bookname.text()
        result.author=self.author.text()
        try:
            self.session.add(result)
            self.session.commit()
            self.close()
        except:
            print("Error occured while saving")
            
class EditBookUI(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title = 'Edit Book'
        self.left = 30
        self.top = 30
        self.width = 500    
        self.height = 500
        self.editWindow=editpopup()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self):
        books=self.session.query(Book).all()
        print(len(books))
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(books)+1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Book Name"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Author"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Action"))
        for i in range(len(books)):
            self.tableWidget.setItem(i+1,0,QTableWidgetItem(str(books[i].id)))
            self.tableWidget.setItem(i+1,1,QTableWidgetItem(books[i].name))
            self.tableWidget.setItem(i+1,2,QTableWidgetItem(books[i].author))
            self.tableWidget.setItem(i+1,3,QTableWidgetItem("Edit"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
       
        
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if(currentQTableWidgetItem.text()=="Edit"):
                row=currentQTableWidgetItem.row()
                item=self.tableWidget.item(row, 0)
                result=self.session.query(Book).filter(Book.id==item.text()).first()
                #pass the value to the edit window
                self.editWindow.setValues(result.id,result.name,result.author)
                self.editWindow.show()
                #show the window
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditBookUI()
    sys.exit(app.exec_())
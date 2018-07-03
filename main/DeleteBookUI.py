import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from config import Session 
from tables import Book

class DeleteBookUI(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title = 'Delete Book'
        self.left = 30
        self.top = 30
        self.width = 500    
        self.height = 500
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
 
    def createTable(self):
        
       # Create table
        self.tableWidget = QTableWidget()
        self.populateTable(self.tableWidget)
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
       
    def populateTable(self,table):
        books=self.session.query(Book).all()
        table.setRowCount(len(books)+1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Book Name"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Author"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Action"))
        for i in range(len(books)):
            table.setItem(i+1,0,QTableWidgetItem(str(books[i].id)))
            table.setItem(i+1,1,QTableWidgetItem(books[i].name))
            table.setItem(i+1,2,QTableWidgetItem(books[i].author))
            table.setItem(i+1,3,QTableWidgetItem("Delete"))
        
     
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if(currentQTableWidgetItem.text()=="Delete"):
                row=currentQTableWidgetItem.row()
                print(row)
                item=self.tableWidget.item(row, 0)
                print(item.text())
                result=self.session.query(Book).filter(Book.id==item.text()).first()
                print("Book Name:"+result.name)
                try:
                    self.session.delete(result)
                    self.session.commit()
                    self.populateTable(self.tableWidget)
                except:
                    print("Error occured while deleting")
 

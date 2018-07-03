import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from config import Session 
from tables import User
from _mysql import result

class DeleteUserUI(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title = 'Delete User'
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
        users=self.session.query(User).all()
        print(len(users))
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(users)+1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Username"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Role"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Action"))
        for i in range(len(users)):
            self.tableWidget.setItem(i+1,0,QTableWidgetItem(str(users[i].id)))
            self.tableWidget.setItem(i+1,1,QTableWidgetItem(users[i].username))
            self.tableWidget.setItem(i+1,2,QTableWidgetItem(users[i].role))
            self.tableWidget.setItem(i+1,3,QTableWidgetItem("Delete"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
       
        
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if(currentQTableWidgetItem.text()=="Delete"):
                row=currentQTableWidgetItem.row()
                item=self.tableWidget.item(row,0)
                print(item.text())
                result=self.session.query(User).filter(User.id==item.text()).first()
                try:
                    self.session.delete(result)
                    self.session.commit()
                    self.tableWidget.update()
                except:
                    print("Error while deleting the user")
 

import sys

from PyQt5.Qt import QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout

from config import Session 
from tables import User


class editpopup(QWidget):
    user_id=""
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
        self.username=QLineEdit(self)
        self.username.move(200,200)
        
        self.password=QLineEdit(self)
        self.password.move(200,240)
        self.password.setEchoMode(QLineEdit.Password)
        
        self.role=QComboBox(self)
        self.role.addItem("Student")
        self.role.addItem("Librarian")
        self.role.addItem("Admin")
        self.role.move(200,280)
        
        self.savechanges=QPushButton("Save changes",self)
        self.savechanges.move(250,350)
        self.savechanges.clicked.connect(self.updateValues)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
    def setValues(self,user_id,user_name,user_password,user_role):
           self.user_id=user_id
           self.username.setText(user_name)
           self.password.setText(user_password)
           self.role.setCurrentText(user_role)
           
    def updateValues(self):
        result=self.session.query(User).filter(User.id==self.user_id).first()
        result.username=self.username.text()
        result.password=self.password.text()
        result.role=self.role.currentText()
        try:
            self.session.add(result)
            self.session.commit()
            self.close()
        except:
            print("Error occured while saving")

class EditUserUI(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title = 'Edit User'
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
                result=self.session.query(User).filter(User.id==item.text()).first()
                #pass the value to the edit window
                self.editWindow.setValues(result.id,result.username,result.password,result.role)
                self.editWindow.show()
                #show the window
 
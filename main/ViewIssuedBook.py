import sys

from PyQt5.Qt import QWidget, QApplication, QTableWidget, QTableWidgetItem, \
    QVBoxLayout

from main.DeleteBookUI import DeleteBookUI
from tables import Issue
from config import Session

class ViewIssuedBooks(QWidget):
    session=Session()
    def __init__(self,id):
        super().__init__()
        self.id=id
        self.title="Admin Panel"
        self.width = 640
        self.height = 400
        self.top = 100
        self.left = 100
        self.initUI()
        
    def initUI(self):
        self.createTable()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()
    
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.populateTable(self.tableWidget)
        self.tableWidget.move(0,0)
        # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)
        
    def populateTable(self,table):
        issue=self.session.query(Issue).filter(Issue.issued_to==self.id).all()
        try:
            table.setRowCount(len(issue)+1)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setItem(0,0, QTableWidgetItem("Id"))
            self.tableWidget.setItem(0,1, QTableWidgetItem("Book"))
            self.tableWidget.setItem(0,2, QTableWidgetItem("Author"))
            for i in range(len(issue)):
                table.setItem(i+1,0,QTableWidgetItem(str(issue[i].id)))
                table.setItem(i+1,1,QTableWidgetItem(issue[i].book.name))
                table.setItem(i+1,2,QTableWidgetItem(issue[i].book.author))
        except:
            print("An error has occured")

app = QApplication(sys.argv)
ex = ViewIssuedBooks(4)
sys.exit(app.exec_())
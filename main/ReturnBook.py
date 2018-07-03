import sys

from PyQt5.Qt import QWidget, QApplication, QTableWidget, QTableWidgetItem,\
    QVBoxLayout
from tables import Issue

from config import Session
from main.DeleteBookUI import DeleteBookUI


class ReturnBook(QWidget):
    session=Session()
    def __init__(self):
        super().__init__()
        self.title="Return Book"
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
        self.tableWidget.doubleClicked.connect(self.on_click)
        
    def populateTable(self,table):
        issue=self.session.query(Issue).all()
        table.setRowCount(len(issue)+1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Id"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Issuer"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Book"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Action"))
        for i in range(len(issue)):
            table.setItem(i+1,0,QTableWidgetItem(str(issue[i].id)))
            table.setItem(i+1,1,QTableWidgetItem(issue[i].user.username))
            table.setItem(i+1,2,QTableWidgetItem(issue[i].book.name))
            table.setItem(i+1,3,QTableWidgetItem("Return"))
    
    
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if(currentQTableWidgetItem.text()=="Return"):
                row=currentQTableWidgetItem.row()
                print(row)
                item=self.tableWidget.item(row,0)
                row_id=item.text()
                print("Row id:"+row_id)
                result=self.session.query(Issue).filter(Issue.id==row_id).first()
                try:
                    self.session.delete(result)
                    self.session.commit()
                    self.populateTable(self.tableWidget)
                except:
                    print("Error occured while deleting")
app = QApplication(sys.argv)
ex = ReturnBook()
sys.exit(app.exec_())
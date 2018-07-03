'''
Created on Jul 3, 2018

@author: Pravesh
'''
from config import Session
from tables import Issue
session=Session()
result=session.query(Issue).filter(Issue.id=="1").first()
print(result)
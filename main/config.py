'''
Created on Jun 18, 2018

@author: Pravesh
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine=create_engine('mysql://root@localhost:3306/pylibrary',echo=True)
Base=declarative_base()
Session=sessionmaker(engine)
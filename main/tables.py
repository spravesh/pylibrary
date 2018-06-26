'''
Created on Jun 18, 2018

@author: Pravesh
'''
#We require three tables 
#1.User table
#2.Books Table
#3.Book Management

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

from config import Base, engine, Session


class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    username=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)
    role=Column(String(255),nullable=False)
    
    def __init__(self,username,password,role):
        self.username=username
        self.password=password
        self.role=role
        

class Book(Base):
    __tablename__="book"
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    author=Column(String(255),nullable=False)
    
    def __init__(self,name,author):
        self.name=name
        self.author=author
        
        
class Issue(Base):
    __tablename__="issue_detail"
    id=Column(Integer,primary_key=True)
    issued_to=Column(Integer,ForeignKey('user.id'))
    user=relationship(User,backref=backref('issue_detail',cascade='delete,all'))
    book_id=Column(Integer,ForeignKey('book.id'))
    book=relationship(Book,backref=backref('issue_detail',cascade='delete,all'))
    
    def __init__(self,issued_to,book_id):
        self.issued_to=issued_to
        self.book_id=book_id
        
        
session=Session()
Base.metadata.create_all(engine)
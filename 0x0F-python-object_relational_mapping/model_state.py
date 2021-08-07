#!/usr/bin/python3
""" python file that contains the class definition of a State and
an instance Base = declarative_base().

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Holberton school as a test for the implementation
of sqlalchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that inherits from Base
    Args:
        None
    Attributes:
        __tablename__: table name
        id: elements id
        name: elements names
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

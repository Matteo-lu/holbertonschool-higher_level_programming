#!/usr/bin/python3
""" python file that contains the class definition of a State and
an instance Base = declarative_base().

This Module is for the project 0x0F. Python - Object-relational
mapping proposed by Holberton school as a test for the implementation
of sqlalchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """City class that inherits from Base
Args:
    None
Attributes:
    __tablename__: table name
            id: elements id
            name: elements names
"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('State.id'), nullable=False)

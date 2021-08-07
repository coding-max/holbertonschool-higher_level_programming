#!/usr/bin/python3
"""contains the class definition of a State and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representation of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, )
    name = Column(String(128), nullable=False)

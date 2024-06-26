#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import create_engine, Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

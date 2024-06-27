#!/usr/bin/python3
"""a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    Database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(Database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_name = State.name.ilike('%a%')

    states = session.query(State).order_by(State.id).filter(filter_name).all()

    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

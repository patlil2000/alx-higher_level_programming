#!/usr/bin/python3
""" a script that deletes all State objects
with a name containing the letter a from the
database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    Database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(Database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.ilike('%a%')).all()

    if states:
        for state in states:
            session.delete(state)
        session.commit()
    else:
        print("No states")
    session.close()

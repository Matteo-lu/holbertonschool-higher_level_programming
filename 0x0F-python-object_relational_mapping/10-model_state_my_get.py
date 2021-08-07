#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State.id).filter(State.name == state_name)
    if instance.first() is not None:
        for element in instance:
            print(element[0])
    else:
        print("Not found")

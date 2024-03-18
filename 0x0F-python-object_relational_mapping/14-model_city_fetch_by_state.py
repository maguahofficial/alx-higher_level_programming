#!/usr/bin/python3
"""This prints State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instancexx in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instancexx[0] + ": (" + str(instancexx[1]) + ") " + instancexx[2])

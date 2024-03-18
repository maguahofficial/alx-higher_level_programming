#!/usr/bin/python3
""" This prints State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    enginex = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(enginex)
    Session = sessionmaker(bind=enginex)
    session = Session()
    new_statex = State(name='Louisiana')
    session.add(new_statex)
    new_instancex = session.query(State).filter_by(name='Louisiana').first()
    print(new_instancex.id)
    session.commit()

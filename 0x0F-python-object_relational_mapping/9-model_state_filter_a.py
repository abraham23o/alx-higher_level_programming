#!/usr/bin/python3

"""
A script that lists the State objects with letter a from the database hbtn_0e_6_usa
Username, password and dbname will be passed as arguments to the script.
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()

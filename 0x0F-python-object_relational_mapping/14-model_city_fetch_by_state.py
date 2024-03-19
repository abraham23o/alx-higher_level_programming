#!/usr/bin/python3

"""
A script that lists all City objects from the database hbtn_0e_14_usa
Username, password and dbname will be passed as arguments to the script.
"""

import sys
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(City, State).join(State, City.state_id == State.id)
              .order_by(City.id).all())

    for city, state in cities:
        print(f'{state.name}: {city.id} {city.name}')

    session.close()

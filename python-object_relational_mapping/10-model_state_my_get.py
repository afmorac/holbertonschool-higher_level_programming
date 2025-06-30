#!/usr/bin/python3
"""
Imprime el ID del estado con el nombre dado
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Crear conexión
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el estado exacto por nombre
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Mostrar resultado
    if state:
        print(state.id)
    else:
        print("Not found")

#!/usr/bin/python3
"""
Agrega el estado 'Louisiana' a la base de datos
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Crear motor de conexión
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear nuevo objeto State
    new_state = State(name="Louisiana")

    # Agregarlo a la base de datos
    session.add(new_state)
    session.commit()

    # Imprimir su ID
    print(new_state.id)

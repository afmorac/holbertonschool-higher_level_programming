#!/usr/bin/python3
"""
Actualiza el estado con id=2 y le cambia el nombre a 'New Mexico'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Crear motor de conexión a la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el estado con id = 2
    state = session.query(State).filter_by(id=2).first()

    # Si existe, actualizar el nombre
    if state:
        state.name = "New Mexico"
        session.commit()

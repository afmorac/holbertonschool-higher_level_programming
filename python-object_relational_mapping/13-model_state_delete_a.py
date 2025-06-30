#!/usr/bin/python3
"""
Elimina todos los estados que contienen la letra 'a' en su nombre
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Conectar con la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todos los estados que contengan la letra 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Eliminar cada uno
    for state in states_to_delete:
        session.delete(state)

    session.commit()

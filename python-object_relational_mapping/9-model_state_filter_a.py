#!/usr/bin/python3
"""
Lista todos los estados que contienen la letra 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Crear conexión con la base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Filtrar estados que contienen 'a'
    estados = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Mostrar resultados
    for estado in estados:
        print(f"{estado.id}: {estado.name}")

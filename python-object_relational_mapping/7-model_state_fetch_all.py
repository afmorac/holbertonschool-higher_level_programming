#!/usr/bin/python3
"""
Este script muestra todos los estados en la base de datos usando SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Crear la conexión al motor de base de datos
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Crear una sesión para interactuar con la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todos los estados ordenados por id
    estados = session.query(State).order_by(State.id).all()

    # Imprimir cada estado con su id
    for estado in estados:
        print(f"{estado.id}: {estado.name}")

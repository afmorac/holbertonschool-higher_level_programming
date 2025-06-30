#!/usr/bin/python3
"""
Este script muestra el primer estado de la base de datos usando SQLAlchemy
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

    # Obtener el primer estado ordenado por id
    estado = session.query(State).order_by(State.id).first()

    # Mostrar resultado o 'Nothing'
    if estado:
        print(f"{estado.id}: {estado.name}")
    else:
        print("Nothing")

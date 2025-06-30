#!/usr/bin/python3
"""
Modelo State: define la clase State mapeada a la tabla 'states'
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instancia base para los modelos
Base = declarative_base()


class State(Base):
    """Clase que representa la tabla 'states' en la base de datos"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

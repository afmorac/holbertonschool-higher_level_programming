#!/usr/bin/python3
"""
Lista todas las ciudades de un estado especificado,
usando una query segura contra inyecciones SQL.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base = sys.argv[3]
    estado = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usuario,
        passwd=clave,
        db=base
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (estado,))

    ciudades = cur.fetchall()
    print(", ".join([ciudad[0] for ciudad in ciudades]))

    cur.close()
    db.close()

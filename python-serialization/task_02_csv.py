#!/usr/bin/env python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convierte datos de un archivo CSV a un archivo JSON llamado 'data.json'.
    Retorna True si fue exitoso, False si ocurre un error (ej: archivo no encontrado).
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False

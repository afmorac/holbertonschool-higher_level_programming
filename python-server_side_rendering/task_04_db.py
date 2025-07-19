from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error leyendo JSON: {e}")
        return []

def read_csv_products():
    products = []
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
    except Exception as e:
        print(f"Error leyendo CSV: {e}")
    return products

def read_sql_products(prod_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if prod_id is not None:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (prod_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]

    except Exception as e:
        print(f"Error con la base de datos: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id', type=int)

    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    elif source == 'sql':
        data = read_sql_products(prod_id)
        if data is None:
            return render_template('product_display.html', error="Database error", products=None)
        if prod_id is not None and not data:
            return render_template('product_display.html', error="Product not found", products=None)

    else:
        return render_template('product_display.html', error="Wrong source", products=None)

    if prod_id is not None and source != 'sql':
        data = [p for p in data if p.get('id') == prod_id]
        if not data:
            return render_template('product_display.html', error="Product not found", products=None)

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

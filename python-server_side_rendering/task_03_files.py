from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id', type=int)

    # Seleccionar fuente
    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    else:
        return render_template('product_display.html', error="Wrong source", products=None)

    # Filtrar si se pidió id
    if prod_id is not None:
        data = [p for p in data if p.get('id') == prod_id]
        if not data:
            return render_template('product_display.html', error="Product not found", products=None)

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

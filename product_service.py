from flask import Flask, jsonify

app = Flask(__name__)

# Baza produktów "na sztywno" w pamięci (słownik)
PRODUCTS = {
    1: {"id": 1, "name": "Laptop", "price": 4500.00},
    2: {"id": 2, "name": "Monitor", "price": 1200.50},
    3: {"id": 3, "name": "Klawiatura mechaniczna", "price": 350.00}
}

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print(f"[Serwis Produktów] Otrzymano zapytanie o produkt ID: {product_id}")
    
    product = PRODUCTS.get(product_id)
    
    if product:
        print(f"[Serwis Produktów] Znaleziono produkt: {product['name']} (200 OK)")
        return jsonify(product), 200
    else:
        print(f"[Serwis Produktów] BŁĄD: Produkt o ID {product_id} nie istnieje (404 Not Found)")
        return jsonify({"error": f"Product with id {product_id} not found"}), 404

if __name__ == '__main__':
    print("Uruchamianie Serwisu Produktów na porcie 8001...")
    app.run(host='localhost', port=8001)
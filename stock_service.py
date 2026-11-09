from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Adres bazowy Serwisu Produktów
PRODUCT_SERVICE_URL = "http://localhost:8001/products"

STOCK = {
    1: 15,
    2: 8,
    3: 0
}

@app.route('/stock/<int:product_id>', methods=['GET'])
def get_stock(product_id):
    print(f"\n[Serwis Magazynowy] Otrzymano zapytanie o stan magazynowy produktu ID: {product_id}")
    print(f"[Serwis Magazynowy] -> Wysyłam zapytanie HTTP GET do Serwisu Produktów ({PRODUCT_SERVICE_URL}/{product_id})...")
    
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
    except requests.exceptions.ConnectionError:
        print("[Serwis Magazynowy] BŁĄD: Brak połączenia z Serwisem Produktów!")
        return jsonify({"error": "Product service is unavailable"}), 503

    if response.status_code == 200:
        product_data = response.json()
        quantity = STOCK.get(product_id, 0)
        print(f"[Serwis Magazynowy] <- Serwis Produktów potwierdził istnienie produktu '{product_data.get('name')}'. Zwracam stan: {quantity} szt. (200 OK)")
        
        return jsonify({
            "productId": product_id,
            "quantity": quantity
        }), 200

    elif response.status_code == 404:
        print(f"[Serwis Magazynowy] <- Serwis Produktów zwrócił 404. Produkt o ID {product_id} nie istnieje! Zwracam 404.")
        return jsonify({
            "error": f"Product with id {product_id} does not exist"
        }), 404

    else:
        return jsonify({"error": "Unexpected error from Product Service"}), response.status_code

if __name__ == '__main__':
    print("Uruchamianie Serwisu Magazynowego na porcie 8002...")
    app.run(host='localhost', port=8002)
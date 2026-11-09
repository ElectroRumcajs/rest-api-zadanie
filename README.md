# System Rozproszony - Komunikacja Mikroserwisów REST API

Projekt przedstawia prosty system rozproszony składający się z dwóch niezależnych mikroserwisów napisanych w języku Python (framework Flask), które komunikują się ze sobą za pomocą protokołu HTTP/REST.

## Architektura i kontrakt API

1. Serwis Produktów (product_service.py)
- Adres i port: http://localhost:8001
- Endpoint: GET /products/{id}
- Odpowiedź (200 OK): {"id": 1, "name": "Laptop", "price": 4500.0}
- Odpowiedź (404 Not Found): Zwracana, gdy produkt o podanym ID nie istnieje.

2. Serwis Magazynowy (stock_service.py)
- Adres i port: http://localhost:8002
- Endpoint: GET /stock/{productId}
- Odpowiedź (200 OK): {"productId": 1, "quantity": 15}
- Odpowiedź (404 Not Found): Zwracana, gdy Serwis Produktów zwróci kod 404 (produkt nie istnieje).

## Instrukcja uruchomienia

1. Utworzenie środowiska wirtualnego i instalacja bibliotek:
   python -m venv venv
   .\venv\Scripts\Activate
   pip install -r requirements.txt

2. Uruchomienie Serwisu Produktów (w pierwszym terminalu):
   python product_service.py

3. Uruchomienie Serwisu Magazynowego (w drugim terminalu):
   python stock_service.py

4. Testowanie działania:
   - Scenariusz sukcesu: GET http://localhost:8002/stock/1 (zwraca 200 OK)
   - Scenariusz błędu: GET http://localhost:8002/stock/99 (zwraca 404 Not Found)
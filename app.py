from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify([
        {"id": 1, "name": "Telefon"},
        {"id": 2, "name": "Bilgisayar"},
        {"id": 3, "name": "Tablet"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

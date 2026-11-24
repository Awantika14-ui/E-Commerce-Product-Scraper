from flask import Flask, request, jsonify
from scraper import scrape_products
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/api/search")
def search():
    query = request.args.get("q", "")

    if not query:
        return jsonify([])

    results = scrape_products(query)

    # fallback if nothing found
    if not results:
        results = [
            {
                "name": "Sample Product",
                "price": "₹999",
                "rating": "4",
                "image": "https://via.placeholder.com/150",
                "link": "#"
            }
        ]

    return jsonify(results)


@app.route("/api/health")
def health():
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(debug=True)

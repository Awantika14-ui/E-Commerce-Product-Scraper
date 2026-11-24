import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_products(query):
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]

        # filter by search query
        if query.lower() not in title.lower():
            continue

        price = item.select_one("p.price_color").text

        rating_class = item.select_one("p.star-rating")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "N/A"

        link = urljoin(url, item.h3.a["href"])
        image = urljoin(url, item.img["src"])

        products.append({
            "name": title,
            "price": price,
            "rating": rating,
            "image": image,
            "link": link
        })

    return products

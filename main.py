import dataclasses
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/allinone")


@dataclasses.dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


def parse_single_product(product: Tag) -> Product:
    product_obj = {
        "title": product.select_one('.title')["title"],
        "description": product.select_one('.description').text
    }

    print('product', product_obj)

def get_home_products():
    text = requests.get(HOME_URL).content
    soup = BeautifulSoup(text, 'html.parser')

    products = soup.select(".card-body")

    return [parse_single_product(product) for product in products]

def main():
    get_home_products()

if __name__ == '__main__':
    main()
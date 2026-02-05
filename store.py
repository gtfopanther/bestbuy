from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        # Wir speichern eine Liste der Produkte im Store
        self.products = list(products)

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        # Entfernt das Produkt aus dem Store (wenn es nicht existiert, Python ValueError)
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        # Gesamtmenge aller Artikel (auch inaktive zählen als Bestand, solange quantity > 0)
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        # Nur aktive Produkte zurückgeben
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        # shopping_list = [(product, quantity), ...]
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

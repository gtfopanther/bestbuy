class Product:
    def __init__(self, name, price, quantity):
        # Validierung
        if name == "":
            raise Exception("Product name cannot be empty.")

        if price < 0:
            raise Exception("Price cannot be negative.")

        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        # Instanzvariablen
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.quantity = quantity

        # Wenn Menge 0 ist → deaktivieren
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        # Fehlerfälle
        if quantity <= 0:
            raise Exception("Purchase quantity must be greater than 0.")

        if not self.active:
            raise Exception("Cannot buy an inactive product.")

        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        # Menge reduzieren
        self.quantity -= quantity

        # Wenn leer → deaktivieren
        if self.quantity == 0:
            self.deactivate()

        # Gesamtpreis zurückgeben
        return quantity * self.price

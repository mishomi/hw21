import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def serialize(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f)

    def deserialize(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return Product(data['name'], data['price'], data['quantity'])

products = [
    Product("კომპიუტერი", 1500, 10),
    Product("ტელევიზორი", 800, 20),
    Product("მობილური ტელეფონი", 600, 15)
]

for i, product in enumerate(products):
    product.serialize(f"product_{i}.json")

for i in range(len(products)):
    product = Product.deserialize(f"product_{i}.json")
    print(f"Product {i + 1}: Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

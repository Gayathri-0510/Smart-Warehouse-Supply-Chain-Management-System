# src/entities/entities.py

class Product:
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

class Warehouse:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Supplier:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Customer:
    def __init__(self, name, email, phone, city):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city

class Order:
    def __init__(self, product_id, warehouse_id, quantity):
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.quantity = quantity
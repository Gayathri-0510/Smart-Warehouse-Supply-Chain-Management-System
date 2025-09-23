from src.dao.product_dao import ProductDAO
from src.entities.entities import Product

class ProductService:
    @staticmethod
    def add_product(name, sku, price):
        product = Product(name, sku, price)
        return ProductDAO.create(product)

    @staticmethod
    def list_products():
        return ProductDAO.read_all().data

    @staticmethod
    def update_product(product_id, fields):
        return ProductDAO.update(product_id, fields)

    @staticmethod
    def delete_product(product_id):
        return ProductDAO.delete(product_id)

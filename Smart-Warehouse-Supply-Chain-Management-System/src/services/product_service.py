from src.dao.product_dao import ProductDAO

class ProductService:
    def __init__(self):
        self.dao = ProductDAO()

    def add_product(self, name, sku, price):
        try:
            return self.dao.create(name, sku, price).data
        except Exception as e:
            return {"error": str(e)}

    def list_products(self):
        try:
            return self.dao.read_all().data
        except Exception as e:
            return {"error": str(e)}

    def update_product(self, product_id, name=None, sku=None, price=None):
        try:
            return self.dao.update(product_id, name, sku, price).data
        except Exception as e:
            return {"error": str(e)}

    def delete_product(self, product_id):
        try:
            return self.dao.delete(product_id).data
        except Exception as e:
            return {"error": str(e)}

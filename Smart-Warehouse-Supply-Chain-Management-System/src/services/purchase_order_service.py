from src.dao.purchase_order_dao import PurchaseOrderDAO

class PurchaseOrderService:
    @staticmethod
    def create_purchase_order(supplier_id, warehouse_id, product_id, quantity):
        if quantity <= 0:
            return {"error": "Quantity must be greater than 0"}
        order_data = {
            "supplier_id": supplier_id,
            "warehouse_id": warehouse_id,
            "product_id": product_id,
            "quantity": quantity
        }
        return PurchaseOrderDAO.create(order_data)

    @staticmethod
    def list_purchase_orders():
        return PurchaseOrderDAO.read_all().data

    @staticmethod
    def update_purchase_order(order_id, fields: dict):
        return PurchaseOrderDAO.update(order_id, fields)

    @staticmethod
    def delete_purchase_order(order_id):
        return PurchaseOrderDAO.delete(order_id)

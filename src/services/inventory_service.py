from src.dao.inventory_dao import InventoryDAO

class InventoryService:
    @staticmethod
    def add_stock(product_id, warehouse_id, quantity):
        try:
            InventoryDAO.add_stock(product_id, warehouse_id, quantity)
            return "Stock added successfully!"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def reduce_stock(product_id, warehouse_id, quantity):
        try:
            InventoryDAO.update_stock(product_id, warehouse_id, -quantity)
            return "Stock reduced!"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def check_stock(product_id, warehouse_id):
        try:
            return InventoryDAO.get_stock(product_id, warehouse_id)
        except Exception as e:
            return 0

    @staticmethod
    def get_stock(product_id, warehouse_id):
        return InventoryService.check_stock(product_id, warehouse_id)

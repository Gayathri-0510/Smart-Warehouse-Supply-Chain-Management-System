from src.dao.inventory_dao import InventoryDAO

class InventoryService:
    @staticmethod
    def add_stock(product_id, warehouse_id, quantity):
        return InventoryDAO.add_stock(product_id, warehouse_id, quantity)

    @staticmethod
    def reduce_stock(product_id, warehouse_id, quantity):
        return InventoryDAO.update_stock(product_id, warehouse_id, -quantity)

    @staticmethod
    def check_stock(product_id, warehouse_id):
        return InventoryDAO.get_stock(product_id, warehouse_id)

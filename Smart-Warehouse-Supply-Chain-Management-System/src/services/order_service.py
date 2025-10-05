# src/services/order_service.py
from src.entities.entities import Order
from src.dao.order_dao import OrderDAO
from src.dao.inventory_dao import InventoryDAO
from src.dao.warehouse_dao import WarehouseDAO

class OrderService:
    @staticmethod
    def place_customer_order(product_id, qty):
        warehouses = WarehouseDAO.read_all().data
        for w in warehouses:
            stock = InventoryDAO.get_stock(product_id, w["warehouse_id"])
            if stock and stock >= qty:
                InventoryDAO.update_stock(product_id, w["warehouse_id"], -qty)
                order = Order(product_id, w["warehouse_id"], qty)
                return OrderDAO.create_customer_order(order)
        return {"error": "Not enough stock!"}

    @staticmethod
    def list_orders():
        return OrderDAO.read_all_customer_orders()

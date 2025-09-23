from src.dao.warehouse_dao import WarehouseDAO
from src.entities.entities import Warehouse

class WarehouseService:
    @staticmethod
    def add_warehouse(name, city):
        warehouse = Warehouse(name, city)
        return WarehouseDAO.create(warehouse)

    @staticmethod
    def list_warehouses():
        return WarehouseDAO.read_all().data

    @staticmethod
    def update_warehouse(warehouse_id, fields):
        return WarehouseDAO.update(warehouse_id, fields)

    @staticmethod
    def delete_warehouse(warehouse_id):
        return WarehouseDAO.delete(warehouse_id)

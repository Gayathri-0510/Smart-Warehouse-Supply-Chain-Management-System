from src.dao.supplier_dao import SupplierDAO
from src.entities.entities import Supplier

class SupplierService:
    @staticmethod
    def add_supplier(name, contact):
        supplier = Supplier(name, contact)
        return SupplierDAO.create(supplier)

    @staticmethod
    def list_suppliers():
        return SupplierDAO.read_all().data

    @staticmethod
    def update_supplier(supplier_id, name=None, contact=None):
        fields = {}
        if name: fields["name"] = name
        if contact: fields["contact"] = contact
        return SupplierDAO.update(supplier_id, fields)

    @staticmethod
    def delete_supplier(supplier_id):
        return SupplierDAO.delete(supplier_id)

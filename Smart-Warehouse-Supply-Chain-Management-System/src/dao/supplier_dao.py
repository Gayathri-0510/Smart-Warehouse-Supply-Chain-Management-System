from src.config import get_supabase
from src.entities.entities import Supplier  # assuming your Supplier class is in entity.py

sb = get_supabase()

class SupplierDAO:
    @staticmethod
    def create(supplier: Supplier):
        return sb.table("suppliers").insert({
            "name": supplier.name,
            "contact": supplier.contact
        }).execute()

    @staticmethod
    def read_all():
        return sb.table("suppliers").select("*").execute()

    @staticmethod
    def update(supplier_id, fields: dict):
        return sb.table("suppliers").update(fields).eq("supplier_id", supplier_id).execute()

    @staticmethod
    def delete(supplier_id):
        return sb.table("suppliers").delete().eq("supplier_id", supplier_id).execute()

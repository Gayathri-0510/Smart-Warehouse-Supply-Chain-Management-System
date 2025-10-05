from src.config import get_supabase

sb = get_supabase()

class WarehouseDAO:
    @staticmethod
    def create(warehouse):
        return sb.table("warehouses").insert({
            "name": warehouse.name,
            "city": warehouse.city
        }).execute()

    @staticmethod
    def read_all():
        return sb.table("warehouses").select("*").execute()

    @staticmethod
    def update(warehouse_id, fields):
        return sb.table("warehouses").update(fields).eq("warehouse_id", warehouse_id).execute()

    @staticmethod
    def delete(warehouse_id):
        return sb.table("warehouses").delete().eq("warehouse_id", warehouse_id).execute()

from src.config import get_supabase

sb = get_supabase()

class PurchaseOrderDAO:
    @staticmethod
    def create(order_data: dict):
        """
        order_data should have:
        supplier_id, warehouse_id, product_id, quantity
        """
        return sb.table("purchase_orders").insert(order_data).execute()

    @staticmethod
    def read_all():
        return sb.table("purchase_orders").select("*").execute()

    @staticmethod
    def update(order_id, fields: dict):
        return sb.table("purchase_orders").update(fields).eq("order_id", order_id).execute()

    @staticmethod
    def delete(order_id):
        return sb.table("purchase_orders").delete().eq("order_id", order_id).execute()

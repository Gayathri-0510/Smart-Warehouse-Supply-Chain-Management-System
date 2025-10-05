from src.config import get_supabase

sb = get_supabase()

class InventoryDAO:
    @staticmethod
    def add_stock(product_id, warehouse_id, qty):
        existing = sb.table("inventory").select("*")\
                     .eq("product_id", product_id)\
                     .eq("warehouse_id", warehouse_id).execute().data
        if existing:
            return sb.table("inventory")\
                     .update({"quantity": existing[0]["quantity"] + qty})\
                     .eq("product_id", product_id)\
                     .eq("warehouse_id", warehouse_id).execute()
        else:
            return sb.table("inventory").insert({
                "product_id": product_id,
                "warehouse_id": warehouse_id,
                "quantity": qty
            }).execute()

    @staticmethod
    def get_stock(product_id, warehouse_id):
        res = sb.table("inventory").select("quantity")\
                .eq("product_id", product_id)\
                .eq("warehouse_id", warehouse_id).execute().data
        if res:
            return res[0]["quantity"]
        return 0

    @staticmethod
    def update_stock(product_id, warehouse_id, qty_change):
        stock = InventoryDAO.get_stock(product_id, warehouse_id)
        new_stock = max(stock + qty_change, 0)
        return sb.table("inventory").update({"quantity": new_stock})\
                 .eq("product_id", product_id)\
                 .eq("warehouse_id", warehouse_id).execute()

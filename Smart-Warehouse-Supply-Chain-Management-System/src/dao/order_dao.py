from src.config import get_supabase
sb = get_supabase()

class OrderDAO:
    @staticmethod
    def create_customer_order(order):
        return sb.table("customer_orders").insert({
            "product_id": order.product_id,
            "warehouse_id": order.warehouse_id,
            "quantity": order.quantity
        }).execute()

    @staticmethod
    def read_all_customer_orders():
        return sb.table("customer_orders").select("*").execute()

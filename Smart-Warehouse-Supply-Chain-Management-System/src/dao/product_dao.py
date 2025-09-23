from src.config import get_supabase

sb = get_supabase()

class ProductDAO:
    @staticmethod
    def create(product):
        return sb.table("products").insert({
            "name": product.name,
            "sku": product.sku,
            "price": product.price
        }).execute()

    @staticmethod
    def read_all():
        return sb.table("products").select("*").execute()

    @staticmethod
    def update(product_id, fields):
        return sb.table("products").update(fields).eq("product_id", product_id).execute()

    @staticmethod
    def delete(product_id):
        return sb.table("products").delete().eq("product_id", product_id).execute()

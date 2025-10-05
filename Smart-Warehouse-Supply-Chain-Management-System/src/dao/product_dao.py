from src.config import get_supabase

class ProductDAO:
    def __init__(self):
        self.sb = get_supabase()

    def create(self, name, sku, price):
        return self.sb.table("products").insert({
            "name": name,
            "sku": sku,
            "price": price
        }).execute()

    def read_all(self):
        return self.sb.table("products").select("*").execute()

    def update(self, product_id, name=None, sku=None, price=None):
        data = {}
        if name: data["name"] = name
        if sku: data["sku"] = sku
        if price is not None: data["price"] = price
        return self.sb.table("products").update(data).eq("id", product_id).execute()

    def delete(self, product_id):
        return self.sb.table("products").delete().eq("id", product_id).execute()

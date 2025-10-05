from src.config import get_supabase
from src.entities.entities import Customer

sb = get_supabase()

class CustomerDAO:
    @staticmethod
    def create(customer: Customer):
        return sb.table("customers").insert({
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "city": customer.city
        }).execute()

    @staticmethod
    def read_all():
        return sb.table("customers").select("*").execute()

    @staticmethod
    def update(customer_id, fields: dict):
        return sb.table("customers").update(fields).eq("customer_id", customer_id).execute()

    @staticmethod
    def delete(customer_id):
        return sb.table("customers").delete().eq("customer_id", customer_id).execute()

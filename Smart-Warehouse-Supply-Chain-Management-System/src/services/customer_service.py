# src/services/customer_service.py
from src.dao.customer_dao import CustomerDAO
from src.entities.entities import Customer  # <- import Customer class here

class CustomerService:
    @staticmethod
    def add_customer(name, email, phone, city):
        customer = Customer(name, email, phone, city)
        return CustomerDAO.create(customer)

    @staticmethod
    def list_customers():
        return CustomerDAO.read_all().data

    @staticmethod
    def update_customer(customer_id, name=None, email=None, phone=None, city=None):
        fields = {}
        if name: fields["name"] = name
        if email: fields["email"] = email
        if phone: fields["phone"] = phone
        if city: fields["city"] = city
        return CustomerDAO.update(customer_id, fields)

    @staticmethod
    def delete_customer(customer_id):
        return CustomerDAO.delete(customer_id)

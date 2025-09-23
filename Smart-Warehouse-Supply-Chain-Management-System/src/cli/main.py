from src.services.product_service import ProductService
from src.services.customer_service import CustomerService
from src.services.warehouse_service import WarehouseService
from src.services.inventory_service import InventoryService
from src.services.supplier_service import SupplierService
from src.services.order_service import OrderService
from src.services.purchase_order_service import PurchaseOrderService

class WarehouseCLI:
    def __init__(self):
        self.product_service = ProductService()
        self.customer_service = CustomerService()
        self.warehouse_service = WarehouseService()
        self.inventory_service = InventoryService()
        self.supplier_service = SupplierService()
        self.order_service = OrderService()
        self.purchase_order_service = PurchaseOrderService()

    def show_menu(self):
        print("\n=== Smart Warehouse System ===")
        print("1. Products CRUD")
        print("2. Customers CRUD")
        print("3. Warehouses CRUD")
        print("4. Inventory CRUD")
        print("5. Suppliers CRUD")
        print("6. Customer Orders CRUD")
        print("7. Purchase Orders CRUD")
        print("8. Exit")

    # ------------------- Products Menu -------------------
    def products_menu(self):
        while True:
            print("\n--- Product Menu ---")
            print("1. Add Product")
            print("2. List Products")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back")
            choice = input("Choice: ")
            if choice == "1":
                name = input("Name: ")
                sku = input("SKU: ")
                price = float(input("Price: "))
                res = self.product_service.add_product(name, sku, price)
                print("Added:", res)
            elif choice == "2":
                products = self.product_service.list_products()
                print("Products:", products)
            elif choice == "3":
                pid = int(input("Product ID: "))
                name = input("New Name (leave blank to skip): ")
                sku = input("New SKU (leave blank to skip): ")
                price = input("New Price (leave blank to skip): ")
                price = float(price) if price else None
                res = self.product_service.update_product(pid, name, sku, price)
                print("Updated:", res)
            elif choice == "4":
                pid = int(input("Product ID: "))
                res = self.product_service.delete_product(pid)
                print("Deleted:", res)
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

    # ------------------- Customers Menu -------------------
    def customers_menu(self):
        while True:
            print("\n--- Customers Menu ---")
            print("1. Add Customer")
            print("2. List Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back")
            choice = input("Choice: ")
            if choice == "1":
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                city = input("City: ")
                res = self.customer_service.add_customer(name, email, phone, city)
                print("Added:", res)
            elif choice == "2":
                customers = self.customer_service.list_customers()
                print("Customers:", customers)
            elif choice == "3":
                cid = int(input("Customer ID: "))
                name = input("New Name (leave blank to skip): ")
                email = input("New Email (leave blank to skip): ")
                phone = input("New Phone (leave blank to skip): ")
                city = input("New City (leave blank to skip): ")
                res = self.customer_service.update_customer(cid, name, email, phone, city)
                print("Updated:", res)
            elif choice == "4":
                cid = int(input("Customer ID: "))
                res = self.customer_service.delete_customer(cid)
                print("Deleted:", res)
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

    # ------------------- Warehouses Menu -------------------
    def warehouses_menu(self):
        while True:
            print("\n--- Warehouses Menu ---")
            print("1. Add Warehouse")
            print("2. List Warehouses")
            print("3. Update Warehouse")
            print("4. Delete Warehouse")
            print("5. Back")
            choice = input("Choice: ")
            if choice == "1":
                name = input("Name: ")
                city = input("City: ")
                res = self.warehouse_service.add_warehouse(name, city)
                print("Added:", res)
            elif choice == "2":
                warehouses = self.warehouse_service.list_warehouses()
                print("Warehouses:", warehouses)
            elif choice == "3":
                wid = int(input("Warehouse ID: "))
                name = input("New Name (leave blank to skip): ")
                city = input("New City (leave blank to skip): ")
                res = self.warehouse_service.update_warehouse(wid, name, city)
                print("Updated:", res)
            elif choice == "4":
                wid = int(input("Warehouse ID: "))
                res = self.warehouse_service.delete_warehouse(wid)
                print("Deleted:", res)
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

    # ------------------- Inventory Menu -------------------
    def inventory_menu(self):
        while True:
            print("\n--- Inventory Menu ---")
            print("1. Add Stock")
            print("2. Check Stock")
            print("3. Reduce Stock")
            print("4. Back")
            choice = input("Choice: ")
            if choice == "1":
                pid = int(input("Product ID: "))
                wid = int(input("Warehouse ID: "))
                qty = int(input("Quantity: "))
                res = self.inventory_service.add_stock(pid, wid, qty)
                print("Added Stock:", res)
            elif choice == "2":
                pid = int(input("Product ID: "))
                wid = int(input("Warehouse ID: "))
                stock = self.inventory_service.check_stock(pid, wid)
                print("Stock:", stock)
            elif choice == "3":
                pid = int(input("Product ID: "))
                wid = int(input("Warehouse ID: "))
                qty = int(input("Quantity to reduce: "))
                res = self.inventory_service.reduce_stock(pid, wid, qty)
                print("Reduced Stock:", res)
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    # ------------------- Suppliers Menu -------------------
    def suppliers_menu(self):
        while True:
            print("\n--- Suppliers Menu ---")
            print("1. Add Supplier")
            print("2. List Suppliers")
            print("3. Update Supplier")
            print("4. Delete Supplier")
            print("5. Back")
            choice = input("Choice: ")
            if choice == "1":
                name = input("Name: ")
                contact = input("Contact: ")
                res = self.supplier_service.add_supplier(name, contact)
                print("Added:", res)
            elif choice == "2":
                suppliers = self.supplier_service.list_suppliers()
                print("Suppliers:", suppliers)
            elif choice == "3":
                sid = int(input("Supplier ID: "))
                name = input("New Name (leave blank to skip): ")
                contact = input("New Contact (leave blank to skip): ")
                res = self.supplier_service.update_supplier(sid, name, contact)
                print("Updated:", res)
            elif choice == "4":
                sid = int(input("Supplier ID: "))
                res = self.supplier_service.delete_supplier(sid)
                print("Deleted:", res)
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

    # ------------------- Customer Orders Menu -------------------
    def customer_orders_menu(self):
        while True:
            print("\n--- Customer Orders Menu ---")
            print("1. Place Customer Order")
            print("2. List Customer Orders")
            print("3. Back")
            choice = input("Choice: ")
            if choice == "1":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                res = self.order_service.place_customer_order(pid, qty)
                print("Order Result:", res)
            elif choice == "2":
                orders = self.order_service.list_orders()
                print("Customer Orders:", orders)
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    # ------------------- Purchase Orders Menu -------------------
    def purchase_orders_menu(self):
        while True:
            print("\n--- Purchase Orders Menu ---")
            print("1. Add Purchase Order")
            print("2. List Purchase Orders")
            print("3. Back")
            choice = input("Choice: ")
            if choice == "1":
                sid = int(input("Supplier ID: "))
                wid = int(input("Warehouse ID: "))
                pid = int(input("Product ID: "))
                qty = int(input("Quantity: "))
                res = self.purchase_order_service.create_purchase_order(sid, wid, pid, qty)
                print("Purchase Order Result:", res)
            elif choice == "2":
                orders = self.purchase_order_service.list_purchase_orders()
                print("Purchase Orders:", orders)
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    # ------------------- Run CLI -------------------
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.products_menu()
            elif choice == "2":
                self.customers_menu()
            elif choice == "3":
                self.warehouses_menu()
            elif choice == "4":
                self.inventory_menu()
            elif choice == "5":
                self.suppliers_menu()
            elif choice == "6":
                self.customer_orders_menu()
            elif choice == "7":
                self.purchase_orders_menu()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    cli = WarehouseCLI()
    cli.run()

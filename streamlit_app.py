import streamlit as st
from src.services.product_service import ProductService
from src.services.customer_service import CustomerService
from src.services.warehouse_service import WarehouseService
from src.services.inventory_service import InventoryService
from src.services.supplier_service import SupplierService
from src.services.order_service import OrderService
from src.services.purchase_order_service import PurchaseOrderService

# Initialize services
product_service = ProductService()
customer_service = CustomerService()
warehouse_service = WarehouseService()
inventory_service = InventoryService()
supplier_service = SupplierService()
order_service = OrderService()
purchase_order_service = PurchaseOrderService()

# Streamlit App Title
st.set_page_config(page_title="Smart Warehouse Management System", layout="wide")
st.title("🏭 Smart Warehouse & Supply Chain Management System")

# Sidebar navigation
menu = st.sidebar.radio(
    "📦 Navigation",
    [
        "Products",
        "Customers",
        "Warehouses",
        "Inventory",
        "Suppliers",
        "Customer Orders",
        "Purchase Orders",
    ],
)

# -------------------------------------------------------------------
# 🛒 PRODUCTS
# -------------------------------------------------------------------
if menu == "Products":
    st.header("🛒 Manage Products")

    with st.expander("➕ Add New Product"):
        name = st.text_input("Product Name")
        sku = st.text_input("SKU")
        price = st.number_input("Price", min_value=0.0)
        if st.button("Add Product"):
            res = product_service.add_product(name, sku, price)
            st.success(f"✅ {res}")

    st.subheader("📋 Product List")
    products = product_service.list_products()
    st.write(products)

# -------------------------------------------------------------------
# 👥 CUSTOMERS
# -------------------------------------------------------------------
elif menu == "Customers":
    st.header("👥 Manage Customers")

    with st.expander("➕ Add Customer"):
        name = st.text_input("Customer Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        city = st.text_input("City")
        if st.button("Add Customer"):
            res = customer_service.add_customer(name, email, phone, city)
            st.success(f"✅ {res}")

    st.subheader("📋 Customer List")
    customers = customer_service.list_customers()
    st.write(customers)

# -------------------------------------------------------------------
# 🏢 WAREHOUSES
# -------------------------------------------------------------------
elif menu == "Warehouses":
    st.header("🏢 Manage Warehouses")

    with st.expander("➕ Add Warehouse"):
        name = st.text_input("Warehouse Name")
        city = st.text_input("City")
        if st.button("Add Warehouse"):
            res = warehouse_service.add_warehouse(name, city)
            st.success(f"✅ {res}")

    st.subheader("🏭 Warehouse List")
    warehouses = warehouse_service.list_warehouses()
    st.write(warehouses)

# -------------------------------------------------------------------
# 📦 INVENTORY
# -------------------------------------------------------------------
elif menu == "Inventory":
    st.header("📦 Manage Inventory")

    with st.expander("➕ Add Stock"):
        pid = st.number_input("Product ID", min_value=1)
        wid = st.number_input("Warehouse ID", min_value=1)
        qty = st.number_input("Quantity", min_value=1)
        if st.button("Add Stock"):
            res = inventory_service.add_stock(pid, wid, qty)
            st.success(f"✅ {res}")

    with st.expander("🔍 Check Stock"):
        pid_check = st.number_input("Product ID (Check)", min_value=1, key="pid_check")
        wid_check = st.number_input("Warehouse ID (Check)", min_value=1, key="wid_check")
        if st.button("Check Stock"):
            res = inventory_service.get_stock(pid_check, wid_check)
            st.info(f"Available Stock: {res}")

# -------------------------------------------------------------------
# 🚚 SUPPLIERS
# -------------------------------------------------------------------
elif menu == "Suppliers":
    st.header("🚚 Manage Suppliers")

    with st.expander("➕ Add Supplier"):
        name = st.text_input("Supplier Name")
        contact = st.text_input("Contact")
        if st.button("Add Supplier"):
            res = supplier_service.add_supplier(name, contact)
            st.success(f"✅ {res}")

    st.subheader("📋 Supplier List")
    suppliers = supplier_service.list_suppliers()
    st.write(suppliers)

# -------------------------------------------------------------------
# 🧾 CUSTOMER ORDERS
# -------------------------------------------------------------------
elif menu == "Customer Orders":
    st.header("🧾 Customer Orders")

    with st.expander("🛍️ Place New Order"):
        pid = st.number_input("Product ID", min_value=1)
        qty = st.number_input("Quantity", min_value=1)
        if st.button("Place Order"):
            res = order_service.place_customer_order(pid, qty)
            st.success(f"✅ {res}")

    st.subheader("📋 Orders List")
    orders = order_service.list_orders()
    st.write(orders)

# -------------------------------------------------------------------
# 📦 PURCHASE ORDERS
# -------------------------------------------------------------------
elif menu == "Purchase Orders":
    st.header("📦 Purchase Orders")

    with st.expander("➕ Add Purchase Order"):
        sid = st.number_input("Supplier ID", min_value=1)
        wid = st.number_input("Warehouse ID", min_value=1)
        pid = st.number_input("Product ID", min_value=1)
        qty = st.number_input("Quantity", min_value=1)
        if st.button("Add Purchase Order"):
            res = purchase_order_service.create_purchase_order(sid, wid, pid, qty)
            st.success(f"✅ {res}")

    st.subheader("📋 Purchase Orders List")
    purchase_orders = purchase_order_service.list_purchase_orders()
    st.write(purchase_orders)

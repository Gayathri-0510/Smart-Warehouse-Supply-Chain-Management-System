# Smart Warehouse & Supply Chain Management System

## Overview
This is a full-stack Streamlit and Python application for managing a smart warehouse and supply chain, with Supabase for database and authentication!

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: Supabase PostgreSQL
- **Dependencies**: streamlit, supabase, python-dotenv

## Installation

1. **Clone or navigate to project directory**
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows activate:
   .\venv\Scripts\activate
   # On macOS/Linux activate:
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up Supabase**:
   - Go to [https://supabase.com/](https://supabase.com/) and create a new project
   - In Supabase, go to **SQL Editor > New Query**, copy the contents of `supabase_schema.sql`, paste it, and run it to create your tables!
   - Get your **Project URL** and **anon/public key** from **Project Settings > API** in Supabase
5. **Configure environment variables**:
   - Open the `.env` file in the project root
   - Replace the example values with your actual Supabase URL and key:
     ```
     SUPABASE_URL=https://your-project-id.supabase.co
     SUPABASE_KEY=your-supabase-anon-public-key
     ```

## How to Run
To start the Streamlit app, use:
```bash
streamlit run streamlit_app.py
# Or if that doesn't work:
python -m streamlit run streamlit_app.py
```

## Features
- **Products**: Add, view, update, delete products
- **Customers**: Manage customer information
- **Warehouses**: Track warehouses and their locations
- **Inventory**: Add, reduce, check stock levels
- **Suppliers**: Manage suppliers
- **Customer Orders**: Place and track customer orders with automatic warehouse selection
- **Purchase Orders**: Manage orders from suppliers

## Project Structure
```
Smart-Warehouse-Supply-Chain-Management-System/
├── streamlit_app.py        # Main application
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
├── .env.example            # Example env file
├── supabase_schema.sql     # SQL schema for Supabase
├── src/
│   ├── config.py           # Supabase configuration
│   ├── entities/           # Data classes
│   │   └── entities.py
│   ├── dao/                # Data Access Objects (database interaction)
│   └── services/           # Business logic layer
```

## Troubleshooting
1. **"streamlit: command not found"**: Use `python -m streamlit run streamlit_app.py` instead
2. **"Could not find the table"**: Make sure you ran the SQL schema in Supabase's SQL Editor
3. **"getaddrinfo failed"**: Check your SUPABASE_URL in .env is correct and project is active
4. **"AttributeError: 'XService' object has no attribute..."**: Refresh your browser or restart the app

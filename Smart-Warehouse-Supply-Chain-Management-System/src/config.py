import streamlit as st
from supabase import create_client, Client

# Get Supabase credentials from Streamlit Secrets
SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY")

def get_supabase() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError(
            "SUPABASE_URL and SUPABASE_KEY must be set as environment variables or in Streamlit Secrets."
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)

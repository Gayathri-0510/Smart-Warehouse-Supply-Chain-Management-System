import socket

host = "zaiuumoyihzahqgpcjdp.supabase.co"
try:
    ip = socket.gethostbyname(host)
    print(f"✅ Host resolves to: {ip}")
except Exception as e:
    print("❌ Cannot resolve host:", e)

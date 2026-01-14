# db/client_supabase.py
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not api_url or not key:
    raise ValueError("Debes definir SUPABASE_URL en el .env")
if not key:
    raise ValueError("Debes definir SUPABASE_KEY en el .env")

# Cliente global de Supabase
supabase = create_client(api_url, key)

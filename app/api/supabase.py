from dotenv import load_dotenv

load_dotenv()

from supabase import create_client, Client
import os



SUPABASE_URL = os.getenv("SUPABASE_URL", None)
SUPABASE_KEY = os.getenv("SUPABASE_KEY", None)
        

     
# Initialize Supabase client
def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase_client: Client = get_supabase_client()


def get_supabase():
    return supabase_client

from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

SUPABASE_URL = "https://qoxfruvulqkfzoqmacqm.supabase.co"
SUPABASE_KEY = "PASTE_YOUR_sb_publishable_KEY_HERE"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"message": "BRONZE HUB B2 API is running!"}

@app.get("/api/finance/summary")
def finance_summary(user_id: str):
    response = supabase.table("finances").select("*").eq("user_id", user_id).execute()

    income = 0
    expense = 0

    for item in response.data:
        if item["type"] == "income":
            income += float(item["amount"])
        else:
            expense += float(item["amount"])

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }

from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

# 🔑 Replace with YOUR keys
SUPABASE_URL = "YOUR_URL"
SUPABASE_KEY = "YOUR_KEY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def home():
    return {"message": "BRONZE HUB B2 API is running!"}

@app.get("/api/finance/summary")
def finance_summary(user_id: str):
    data = supabase.table("finances").select("*").eq("user_id", user_id).execute()

    income = 0
    expense = 0

    for item in data.data:
        if item["type"] == "income":
            income += item["amount"]
        else:
            expense += item["amount"]

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }

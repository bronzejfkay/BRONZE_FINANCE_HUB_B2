from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "BRONZE HUB B2 API is running!"}

@app.get("/api/finance/summary")
def finance_summary(user_id: str):
    return {
        "user_id": user_id,
        "income": 0,
        "expense": 0,
        "balance": 0
    }

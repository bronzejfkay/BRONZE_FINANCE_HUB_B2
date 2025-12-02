from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "BRONZE HUB B2 API is running!"}

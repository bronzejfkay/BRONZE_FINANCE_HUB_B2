# BRONZE FINANCE HUB — Backend (B2 Advanced)

This package contains a FastAPI backend with mock prediction logic for:
- Personal finance tracking
- Stock prediction (mock)
- Forex prediction (mock)
- Sports odds prediction (mock)

## How to run locally
1. python -m venv venv
2. source venv/bin/activate  (mac/linux) or venv\Scripts\activate (windows)
3. pip install -r requirements.txt
4. uvicorn app.main:app --host 0.0.0.0 --port 8000

## Deta Space deploy
- Spacefile included (runtime python3.10)
- Deta will run: pip install -r requirements.txt then `python -m app.main`

from fastapi import FastAPI

from routes.routes_scraper import router as scraper_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

app.include_router(scraper_router, prefix="/scraper", tags=["scraper"])

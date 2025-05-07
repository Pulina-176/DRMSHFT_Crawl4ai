from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from services.scraper import crawler as scraper_service

router = APIRouter()

@router.get("/test")
async def scrape_test():
    try:
        # Call the scraper service function
        result = await scraper_service()
        return JSONResponse(content="test", status_code=200)
    except Exception as e:
        # Handle any exceptions that occur during scraping
        raise HTTPException(status_code=500, detail=str(e))
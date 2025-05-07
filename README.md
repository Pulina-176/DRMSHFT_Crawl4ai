# DRMSHFT_Crawl4ai
Crawl4ai Web Crawler for DreamShift-Assist

## Step 1: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows

## Step 2: Install dependencies
pip install -r requirements.txt

## Step 3: Run the app
uvicorn main:app

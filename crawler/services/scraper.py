import asyncio
import os
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler, BrowserConfig, ProxyConfig, CrawlerRunConfig, CacheMode

load_dotenv()

# Bright Data's Web Unlocker API proxy configuration
proxy_config = ProxyConfig(
    server=os.getenv("PROXY_SERVER"),
    username=os.getenv("PROXY_USERNAME"),
    password=os.getenv("PROXY_PASSWORD")
)


async def crawler(role: str = "software engineer", location: str = "Colombo, Sri Lanka"):

    # Browser configuration
    browser_config = BrowserConfig(
        headless=True,
        proxy_config=proxy_config
    )

    # Crawler configuration
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        wait_until="domcontentloaded", # wait until the DOM of the page has been loaded
        page_timeout=180000, # wait up to 3 mins for page load
    )

    # Run the AI-powered crawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=f"https://www.google.com/search?q={role}+jobs+in+{location}&ibp=htl;jobs",
            config=crawler_config
        )

        # print the first 1000 characters
        print(f"Parsed Markdown data:\n{result.markdown[:1000]}")
        print(f"Response status code: {result.status_code}")

if __name__ == "__main__":
    asyncio.run(crawler())
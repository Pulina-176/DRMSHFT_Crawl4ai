import asyncio
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

load_dotenv()

async def crawler():
    # Browser configuration
    browser_config = BrowserConfig(
        headless=True
    )

    # Crawler configuration
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS
    )

    # Run the AI-powered crawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://dev.to/jay_sheth/deploy-host-a-react-application-on-nginx-with-ubuntu-m4l",
            config=crawler_config
        )

        # print the first 1000 characters
        print(f"Parsed Markdown data:\n{result.markdown[:1000]}")
        print(f"Response status code: {result.status_code}")

if __name__ == "__main__":
    asyncio.run(crawler())
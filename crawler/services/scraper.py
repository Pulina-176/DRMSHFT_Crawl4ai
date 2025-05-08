import asyncio
import os
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler, BrowserConfig, ProxyConfig, CrawlerRunConfig, CacheMode, LLMExtractionStrategy, LLMConfig
from models.jobs import Job

load_dotenv()

# Bright Data's Web Unlocker API proxy configuration
proxy_config = ProxyConfig(
    server=os.getenv("PROXY_SERVER"),
    username=os.getenv("PROXY_USERNAME"),
    password=os.getenv("PROXY_PASSWORD")
)

extraction_strategy = LLMExtractionStrategy(
        llm_config=LLMConfig(provider=os.getenv("LLM_MODEL"), api_token=os.getenv("LLM_API_TOKEN")),
        schema=Job.model_json_schema(),
        extraction_type="schema",
        instruction=(
            """Extract all links to the jobs-detail-viewer of each respective google job in the page. Scroll and extract all the links possible."""
        ),
        input_format="markdown",
        verbose=True
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
        css_selector="[class^='MQUd2b']",
        extraction_strategy=extraction_strategy
    )

    # Run the AI-powered crawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=f"https://www.google.com/search?q={role}+jobs+in+{location}&ibp=htl;jobs",
            config=crawler_config
        )

        # print the first 1000 characters
        print(f"Parsed Markdown data:\n{result}")
        print(f"Response status code: {result.status_code}")
        print(f"Length of list: {len(result)}")

        return result.markdown[:1000]

if __name__ == "__main__":
    asyncio.run(crawler())
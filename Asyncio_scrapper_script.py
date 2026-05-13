import asyncio
import httpx
import time

# List of websites to "ping" (fetch headers)
URLS = [
    "https://www.google.com", "https://www.github.com", "https://www.python.org",
    "https://www.reddit.com", "https://www.stackoverflow.com", "https://www.wikipedia.org",
    "https://www.apple.com", "https://www.amazon.com", "https://www.microsoft.com",
    "https://www.netflix.com"
]

async def ping_site(client, url):
    """Pings a single site and returns the response time."""
    start_time = time.perf_counter()
    try:
        # We use .get() but could use .head() to save bandwidth
        response = await client.get(url, timeout=5.0)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"✅ {url:30} | Status: {response.status_code} | Time: {duration:.3f}s")
        return duration
    except Exception as e:
        print(f"❌ {url:30} | Failed: {e}")
        return None

async def main():
    print(f"Starting pings on {len(URLS)} sites...\n")
    start_total = time.perf_counter()

    # Use a single client for all requests (connection pooling)
    async with httpx.AsyncClient() as client:
        # Create a list of tasks to run concurrently
        tasks = [ping_site(client, url) for url in URLS]
        
        # 'gather' runs them all at once and waits for the results
        results = await asyncio.gather(*tasks)

    end_total = time.perf_counter()
    valid_results = [r for r in results if r is not None]
    
    print(f"\n--- Statistics ---")
    print(f"Total time elapsed:  {end_total - start_total:.3f}s")
    if valid_results:
        print(f"Average response:    {sum(valid_results)/len(valid_results):.3f}s")

if __name__ == "__main__":
    asyncio.run(main())
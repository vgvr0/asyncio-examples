import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'http://example.com/1',
        'http://example.com/2',
        'http://example.com/3'
    ]
    
    # Schedule all fetch coroutines to run concurrently.
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    # Process the results
    for content in results:
        print(content)

# Run the main function
asyncio.run(main())

import asyncio
import aiohttp
import aiofiles

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def write_to_file(filename, content):
    async with aiofiles.open(filename, 'w') as f:
        await f.write(content)

async def main():
    urls = [
        'https://example.com/data1',
        'https://example.com/data2',
        'https://example.com/data3'
    ]
    output_files = [
        'output1.txt',
        'output2.txt',
        'output3.txt'
    ]

    # Create a session for making HTTP requests
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url, output_file in zip(urls, output_files):
            # Fetch each URL and write its content to a corresponding file
            content = await fetch_url(session, url)
            tasks.append(write_to_file(output_file, content))
        
        # Wait for all file writing operations to complete
        await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())

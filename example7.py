import asyncio
import aiohttp
import aiofiles

# Asynchronous function to fetch data from a URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Asynchronous function to save data to a file
async def save_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as f:
        await f.write(data)

# Main coroutine that manages other tasks
async def main():
    # List of URLs to fetch data from
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net'
    ]
    
    # List to hold the content from URLs
    contents = []
    
    # Create an instance of a session
    async with aiohttp.ClientSession() as session:
        # Schedule all fetch operations to run concurrently
        fetch_tasks = [fetch(session, url) for url in urls]
        contents = await asyncio.gather(*fetch_tasks)
    
    # Schedule all file writing operations to run concurrently
    save_tasks = [save_to_file(f'file_{index}.txt', content)
                  for index, content in enumerate(contents)]
    
    # Wait until all save tasks are completed
    await asyncio.gather(*save_tasks)

# Run the main coroutine

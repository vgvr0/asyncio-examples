import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Executed in {end - start:.2f} seconds.")

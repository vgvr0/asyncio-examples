import asyncio

async def tarea1():
    await asyncio.sleep(1)  # Simula una operación I/O
    return 'Resultado de tarea1'

async def tarea2():
    await asyncio.sleep(2)  # Simula una operación I/O
    return 'Resultado de tarea2'

async def main():
    resultado1 = await tarea1()
    print(resultado1)
    resultado2 = await tarea2()
    print(resultado2)

# Python 3.7+
asyncio.run(main())

# Para Python 3.6
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

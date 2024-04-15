import asyncio

# Definimos varias corrutinas
async def tarea_lenta(numero):
    print(f"Tarea {numero} iniciada, esperará 3 segundos.")
    await asyncio.sleep(3)
    print(f"Tarea {numero} completada.")

async def tarea_rapida(numero):
    print(f"Tarea {numero} iniciada, esperará 1 segundo.")
    await asyncio.sleep(1)
    print(f"Tarea {numero} completada.")

# Función principal que ejecuta las corrutinas
async def main():
    # Creamos las tareas para las corrutinas
    tarea1 = asyncio.create_task(tarea_lenta(1))
    tarea2 = asyncio.create_task(tarea_rapida(2))
    tarea3 = asyncio.create_task(tarea_rapida(3))

    # Esperamos a que todas las tareas se completen
    await tarea1
    await tarea2
    await tarea3

# Ejecutamos el bucle de eventos
asyncio.run(main())

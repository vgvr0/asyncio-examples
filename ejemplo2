import asyncio

# Definimos las funciones asíncronas
async def tarea_lenta(numero):
    print(f"Tarea {numero} iniciada, esperará 3 segundos.")
    await asyncio.sleep(3)
    print(f"Tarea {numero} completada.")

async def tarea_rapida(numero):
    print(f"Tarea {numero} iniciada, esperará 1 segundo.")
    await asyncio.sleep(1)
    print(f"Tarea {numero} completada.")

# Función principal que ejecuta las funciones asíncronas
async def main():
    # Creamos tareas para cada función asíncrona
    tarea1 = asyncio.create_task(tarea_lenta(1))
    tarea2 = asyncio.create_task(tarea_rapida(2))
    tarea3 = asyncio.create_task(tarea_rapida(3))

    # Esperamos a que todas las tareas se completen
    await asyncio.gather(tarea1, tarea2, tarea3)

# Ejecutamos el bucle de eventos
asyncio.run(main())

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
    await tarea_lenta(1)
    await tarea_rapida(2)
    await tarea_rapida(3)

# Ejecutamos el bucle de eventos
asyncio.run(main())

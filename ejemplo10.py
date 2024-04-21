import asyncio

class AsyncioEjemplo:
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    async def tarea_asincrona(self, delay, nombre):
        await asyncio.sleep(delay)
        print(f'Tarea {nombre} completada después de {delay} segundos')

    def ejecutar_tareas(self):
        try:
            asyncio.run(self.main())
        except RuntimeError:  # asyncio.run() no puede ser llamado desde un running event loop
            self.loop.run_until_complete(self.main())

    async def main(self):
        tarea1 = asyncio.create_task(self.tarea_asincrona(2, 'A'))
        tarea2 = asyncio.create_task(self.tarea_asincrona(3, 'B'))
        tarea3 = asyncio.create_task(self.tarea_asincrona(1, 'C'))

        await tarea1
        await tarea2
        await tarea3

# Crear una instancia de la clase y ejecutar las tareas
ejemplo = AsyncioEjemplo()
ejemplo.ejecutar_tareas()

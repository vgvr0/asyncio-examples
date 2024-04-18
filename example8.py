import asyncio

class AsincronoDemo:
    def __init__(self, nombre):
        self.nombre = nombre

    async def tarea_asincrona(self):
        print(f'Tarea iniciada: {self.nombre}')
        # Simula una operación que tarda 1 segundo
        await asyncio.sleep(1)
        print(f'Tarea completada: {self.nombre}')

# Función para ejecutar las tareas asíncronas
async def main():
    # Crea una instancia de la clase
    demo = AsincronoDemo('MiTareaAsincrona')
    
    # Ejecuta la tarea asíncrona
    await demo.tarea_asincrona()

# Ejecuta el loop de eventos de asyncio
asyncio.run(main())

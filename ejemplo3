import time

# Definimos varias funciones síncronas
def tarea_lenta(numero):
    print(f"Tarea {numero} iniciada, esperará 3 segundos.")
    time.sleep(3)  # Bloquea la ejecución por 3 segundos
    print(f"Tarea {numero} completada.")

def tarea_rapida(numero):
    print(f"Tarea {numero} iniciada, esperará 1 segundo.")
    time.sleep(1)  # Bloquea la ejecución por 1 segundo
    print(f"Tarea {numero} completada.")

# Función principal que ejecuta las funciones síncronas
def main():
    # Ejecutamos las funciones síncronas una tras otra
    tarea_lenta(1)
    tarea_rapida(2)
    tarea_rapida(3)

# Ejecutamos la función principal
main()

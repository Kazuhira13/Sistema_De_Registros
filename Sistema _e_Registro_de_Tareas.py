import json

tareas_pendientes_text = "tareas_pendientes.txt"
tareas_completadas_text = "tareas_completadas.txt"

def cargar_tareas(archivo):
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas, archivo):
    with open(archivo, "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(tareas):
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    
    nueva_tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False,
    }
    
    tareas.append(nueva_tarea)
    print("Tarea agregada con éxito.")

def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas para mostrar.")
    else:
        for x, tarea in enumerate(tareas, start=1):
            print(f"Tarea {x}:")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print()

def marcar_completada(tareas_pendientes, tareas_completadas):
    listar_tareas(tareas_pendientes)
    if not tareas_pendientes:
        return
    
    try:
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice < len(tareas_pendientes):
            tarea_completada = tareas_pendientes.pop(indice)
            tarea_completada["completada"] = True
            tareas_completadas.append(tarea_completada)
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

def main():
    tareas_pendientes = cargar_tareas(tareas_pendientes_text)
    tareas_completadas = cargar_tareas(tareas_completadas_text)

    while True:
        print("\n--- Menú ---")
        print("1. Agregar Tarea")
        print("2. Listar Tareas Pendientes")
        print("3. Marcar Tarea como Completada")
        print("4. Listar Tareas Completadas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea(tareas_pendientes)
        elif opcion == "2":
            print("\n--- Tareas Pendientes ---")
            listar_tareas(tareas_pendientes)
        elif opcion == "3":
            marcar_completada(tareas_pendientes, tareas_completadas)
        elif opcion == "4":
            print("\n--- Tareas Completadas ---")
            listar_tareas(tareas_completadas)
        elif opcion == "5":
            guardar_tareas(tareas_pendientes, tareas_pendientes_text)
            guardar_tareas(tareas_completadas, tareas_completadas_text)
            print("Gracias por usar el Sistema de Registro de Tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#B 4


#Funcion 
def consultar_articulaciones_robot():
    robots_info = {
        "1": {
            "nombre": "Cartesiano",
            "articulaciones": "3 articulaciones Prismáticas ",
        },
        "2": {
            "nombre": "Cilíndrico",
            "articulaciones": "1 articulación Rotacional y 2 articulaciones Prismáticas ",
        },
        "3": {
            "nombre": "Esférico ",
            "articulaciones": "2 articulaciones Rotacionales y 1 articulación Prismática ",
        }
    }
    
    print("Que robot deseas consultar?")
    print("1. Robot Cartesiano")
    print("2. Robot Cilíndrico")
    print("3. Robot Esférico")
    
    opcion = input("\nSeleccione el número del robot que desea consultar: ").strip()
    

    if opcion in robots_info:
        robot_seleccionado = robots_info[opcion]
        print(f"\n...Robot {robot_seleccionado['nombre']}...")
        print(f"Tipo y número de articulaciones: {robot_seleccionado['articulaciones']}")
        
    else:
        print("\nOpción no válida. Por favor intente de nuevo")

# Main
consultar_articulaciones_robot()

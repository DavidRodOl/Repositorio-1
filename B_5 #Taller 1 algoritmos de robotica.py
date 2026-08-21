#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#B 5

#Funcion 
def bucle_troll():
    print("SYSTEM MESSAGE")
    while True:
        respuesta = input("¿Desea continuar Si/No?\n").strip().lower()

        if respuesta == "no":
            print("Congrats saliste del bucle :)\n")
            break
        
        elif respuesta == "si":
            print("ou nou encarcelado :(\n")
            
        else:
            print("Opción no válida. Por favor intente de nuevo\n")

# Main
bucle_troll()


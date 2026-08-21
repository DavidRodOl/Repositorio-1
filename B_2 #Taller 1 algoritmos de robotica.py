#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#B 2

#Importar librerias
import random

#Funcion 
def generador():
    cantidad = int(input("Cuantos numeros aleatorios quiere generar?: "))
    lim_inferior = int(input("Ingrese el limite inferior para el rango de numeros: "))
    lim_superior = int(input("Ingrese el limite superior para el rango de numeros: "))
    
    if lim_inferior > lim_superior:
        print("verifica que el limite superior sea mayor al limite inferior.")
        return
    
    for i in range(cantidad):
        numero_random = random.randint(lim_inferior, lim_superior)
        print(f"Numero {i+1}: {numero_random}")
#Main 
generador()

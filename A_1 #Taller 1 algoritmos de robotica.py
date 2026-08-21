 #Taller 1 algoritmos de robotica 
 #David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
 #A.1

#Importacion de librerias
import numpy as np 

#Inicializacion de variables
vector1 = np.array([60,80,206])
vector2 = np.array([10,100,212])

#Funciones
def sumar_vectores(v1, v2):
    resultado = v1 + v2
    return resultado

def restar_vectores(v1, v2):
    resultado = v1 - v2
    return resultado

def multiplicar_punto(v1, v2):
    resultado = np.dot(v1, v2)
    return resultado

def multiplicar_cruz(v1, v2):
    resultado = np.cross(v1, v2)
    return resultado

def dividir_vectores(v1, v2):
    resultado = v1 / v2
    return resultado

#impresion de resultados (Main)

resultado_suma = sumar_vectores(vector1, vector2)
print("la suma es:", resultado_suma)

resultado_resta = restar_vectores(vector1, vector2)
print("la resta es:", resultado_resta)

resultado_ppunto = multiplicar_punto(vector1, vector2)
print("el producto punto es:", resultado_ppunto)

resultado_pcruz = multiplicar_cruz(vector1, vector2)
print("el producto cruz es:", resultado_pcruz)

resultado_division = dividir_vectores(vector1, vector2)
print("la division es:", resultado_division)
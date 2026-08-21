 #Taller 1 algoritmos de robotica 
 #David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
 #A.2

#Importacion de librerias
import numpy as np 

#Inicializacion de variables
matriz1 = np.array([[2,8,6],
                   [3,7,5],
                   [8,1,6]])

matriz2 = np.array([[12,23,34],
                   [98,87,76],
                   [67,56,19]])

#Funciones
def sumar_matrices(m1, m2):
    resultado = m1 + m2
    return resultado

def restar_matrices(m1, m2):
    resultado = m1 - m2
    return resultado

def matriz_multiplicar_punto(m1, m2):
    resultado = np.dot(m1, m2)
    return resultado

def matriz_multiplicar_cruz(m1, m2):
    resultado = np.cross(m1, m2)
    return resultado

def dividir_matrices(m1, m2):
    resultado = m1 / m2
    return resultado

#impresion de resultados (Main)
resultado_suma = sumar_matrices(matriz1, matriz2)
print("la suma es:", resultado_suma)

resultado_resta = restar_matrices(matriz1, matriz2)
print("la resta es:", resultado_resta)

resultado_ppunto = matriz_multiplicar_punto(matriz1, matriz2)
print("el producto punto es:", resultado_ppunto)

resultado_pcruz = matriz_multiplicar_cruz(matriz1, matriz2)
print("el producto cruz es:", resultado_pcruz)

resultado_division = dividir_matrices(matriz1, matriz2)
print("la division es:", resultado_division)
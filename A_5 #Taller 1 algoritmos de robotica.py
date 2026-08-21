#Taller 1 algoritmos de robotica 
#David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
#A.5

import numpy as np

angulo = 45

def rotacion_x(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    return R

def rotacion_y(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([[np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    return R

def rotacion_z(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return R  

print("Matriz de rotación en X:\n", rotacion_x(angulo))
print("\nMatriz de rotación en Y:\n", rotacion_y(angulo))
print("\nMatriz de rotación en Z:\n", rotacion_z(angulo))
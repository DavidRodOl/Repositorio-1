 #Taller 1 algoritmos de robotica 
 #David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
 #A.3

import numpy as np

#Inicializacion variables (Formula de Callendar-Van Dusen)
R0 = 100 
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
T = 60

def calcular_resistencia(T):
    if T >= 0:
        R = R0 * (1 + (A * T) + (B * (T**2)))
    else:
        R = R0 * (1 + (A * T) + (B * (T**2)) + (C * (T - 100) * (T**3)))
    return R

resistencia_actual = calcular_resistencia(T)
print("A una temperatura de", T,"grados, el PT100 tiene una resistencia de", round(resistencia_actual, 2),"ohms")

#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#C 1

#Iportar librerias 
import numpy as np
import matplotlib.pyplot as plt

#Constantes de la ecuacion
R0 = 100.0
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

def calcular_resistencia_pt100(t):
    
    r = np.zeros_like(t)
    
    tem_negativas = t < 0
    
    r[tem_negativas] = R0 * (1 + A * t[tem_negativas] + B * (t[tem_negativas]**2) + C * (t[tem_negativas] - 100) * (t[tem_negativas]**3))
    
    tem_positivas = t >= 0

    r[tem_positivas] = R0 * (1 + A * t[tem_positivas] + B * (t[tem_positivas]**2))
    
    return r


temperaturas = np.linspace(-200, 200, 401)


resistencias = calcular_resistencia_pt100(temperaturas)

#Graficacion
plt.figure(figsize=(8, 5))
plt.plot(temperaturas, resistencias, color='blue', linewidth=2, label='Curva PT100')
plt.title("Curva de Comportamiento del Sensor PT100 (-200°C a 200°C)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohmios - Ω)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

#Display
plt.show()

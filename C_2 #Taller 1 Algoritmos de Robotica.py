#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#C 2

#Importar librerias 
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import signal  

def sistema_segundo_orden():
    print("Sistema de Segundo Orden")
    
    k = float(input("Ingrese la ganancia K: "))
    wn = float(input("Ingrese la frecuencia natural Wn (rad/s): "))
    zeta = float(input("Ingrese el factor de amortiguamiento Zeta: "))
    
    if zeta < 1:
        tipo = "Subamortiguado"
    elif zeta == 1:
        tipo = "Criticamente amortiguado"
    else:
        tipo = "Sobreamortiguado"
    
    print(f"Tipo de sistema: {tipo}")
    
    #Coeficientes de la ecuacion diferencial ( Wn y Z )
    a = 1
    b = 2 * zeta * wn
    c = wn**2
    entrada = k * wn**2
    
    #Ventana de tiempo y pasos segun que tan rapido o lento se mueve el sistema
    if zeta > 1:
        p1 = zeta * wn - wn * np.sqrt(zeta**2 - 1)
        p2 = zeta * wn + wn * np.sqrt(zeta**2 - 1)
        tf = ( 8 / p1 )*2
        n = int(max(2000, 60 * (p2 / p1)))
    else:
        tf = (10 / wn)*2
        n = 2000
    
    num = [entrada]
    den = [a, b, c]
    sistema = signal.TransferFunction(num, den)
    t = np.linspace(0, tf, n + 1)
    t, y = signal.step(sistema, T=t)
    
    #Graficacion
    plt.figure(figsize=(8, 5))
    plt.plot(t, y, 'b-', label='Respuesta al escalon', linewidth=2)
    plt.axhline(k, color='r', linestyle='--', label=f'Valor final = {k:.4f}')
    plt.title(f'Respuesta del Sistema - {tipo}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    
    plt.show(block=True) 

#Main
sistema_segundo_orden()

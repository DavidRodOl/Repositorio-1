#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#C 2

#Importar librerias 
import numpy as np
import matplotlib.pyplot as plt

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
    
    #Coeficientes de la ecuacion diferencial a partir de Wn y Zeta
    a = 1
    b = 2 * zeta * wn
    c = wn**2
    entrada = k * wn**2
    
    #Ventana de tiempo y pasos segun que tan rapido o lento se mueve el sistema
    if zeta > 1:
        p1 = zeta * wn - wn * np.sqrt(zeta**2 - 1)
        p2 = zeta * wn + wn * np.sqrt(zeta**2 - 1)
        tf = 8 / p1
        n = int(max(2000, 60 * (p2 / p1)))
    else:
        tf = 10 / wn
        n = 2000
    
    #Simulacion de la respuesta al escalon (Runge-Kutta 4)
    dt = tf / n
    t = np.linspace(0, tf, n + 1)
    y = np.zeros(n + 1)
    dy = np.zeros(n + 1)
    
    for i in range(n):
        k1y, k1dy = dy[i], (entrada - b * dy[i] - c * y[i]) / a
        k2y, k2dy = dy[i] + 0.5*dt*k1dy, (entrada - b*(dy[i]+0.5*dt*k1dy) - c*(y[i]+0.5*dt*k1y)) / a
        k3y, k3dy = dy[i] + 0.5*dt*k2dy, (entrada - b*(dy[i]+0.5*dt*k2dy) - c*(y[i]+0.5*dt*k2y)) / a
        k4y, k4dy = dy[i] + dt*k3dy, (entrada - b*(dy[i]+dt*k3dy) - c*(y[i]+dt*k3y)) / a
        
        y[i+1] = y[i] + (dt/6) * (k1y + 2*k2y + 2*k3y + k4y)
        dy[i+1] = dy[i] + (dt/6) * (k1dy + 2*k2dy + 2*k3dy + k4dy)
    
    #Graficacion
    plt.figure(figsize=(8, 5))
    plt.plot(t, y, 'b-', label='Respuesta al escalon', linewidth=2)
    plt.axhline(k, color='r', linestyle='--', label=f'Valor final = {k:.4f}')
    plt.title(f'Respuesta del Sistema - {tipo}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.show()

#Main
sistema_segundo_orden()
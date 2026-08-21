#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#C 3

#Iportar librerias 
import numpy as np
import matplotlib.pyplot as plt

def circuito_rc():
    print("Circuito RC")
    
    v = float(input("Ingrese el voltaje de la fuente (V): "))
    c = float(input("Ingrese la capacitancia en microfaradios (µF): "))
    r = float(input("Ingrese la resistencia en ohmios (Ω): "))
    
    c = c * 1e-6  
    tau = r * c         
    
    print(f"Tau: {tau:.6f} segundos")
    
    tf = 5 * tau
    t = np.linspace(0, tf, 1000)
    v_carga = v * (1 - np.exp(-t / tau))
    v_descarga = v * np.exp(-t / tau)
    
    #Graficacion
    plt.figure(figsize=(10, 5))
    #carga
    plt.subplot(1, 2, 1)
    plt.plot(t, v_carga, 'b-', label='Carga $V_c(t)$', linewidth=2)
    plt.axvline(tau, color='r', linestyle='--', label=f'Tau = {tau:.4f}s')
    plt.title('Carga del Capacitor')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.grid(True)
    plt.legend()
    
    #descarga
    plt.subplot(1, 2, 2)
    plt.plot(t, v_descarga, 'g-', label='Descarga $V_c(t)$', linewidth=2)
    plt.axvline(tau, color='r', linestyle='--', label=f'Tau = {tau:.4f}s')
    plt.title('Descarga del Capacitor')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

#Main
circuito_rc()

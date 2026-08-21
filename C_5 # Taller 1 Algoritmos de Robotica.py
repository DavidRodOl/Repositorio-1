# Taller 1 Algoritmos de Robotica 
# David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
# C 5

import numpy as np
import matplotlib.pyplot as plt

def dibujar_nombres():
   
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    #Grafica DAVID

    ax1.plot([0, 0], [0, 4], 'b-', linewidth=3)
    theta = np.linspace(-np.pi/2, np.pi/2, 100)
    ax1.plot(0 + 1.2*np.cos(theta), 2 + 2*np.sin(theta), 'b-', linewidth=3)
    
    ax1.plot([2, 3, 4], [0, 4, 0], 'b-', linewidth=3)
    ax1.plot([2.5, 3.5], [2, 2], 'b-', linewidth=3)
    
    ax1.plot([4.5, 5.5, 6.5], [4, 0, 4], 'b-', linewidth=3)
    
    ax1.plot([7.2, 7.2], [0, 4], 'b-', linewidth=3)
    
    ax1.plot([8, 8], [0, 4], 'b-', linewidth=3)
    ax1.plot(8 + 1.2*np.cos(theta), 2 + 2*np.sin(theta), 'b-', linewidth=3)
    
    ax1.set_title("Trayectoria 2D - DAVID", fontsize=14, fontweight='bold')
    ax1.set_xlim(-1, 10)
    ax1.set_ylim(-1, 5)
    ax1.set_aspect('equal') 
    ax1.grid(True, linestyle='--')

    #grafica ROBIN
    
    ax2.plot([0, 0], [0, 4], 'g-', linewidth=3)
    ax2.plot(0 + 1.1*np.cos(theta), 3 + 1*np.sin(theta), 'g-', linewidth=3)
    ax2.plot([0, 1.1], [2, 0], 'g-', linewidth=3)
    
    theta_completo = np.linspace(0, 2*np.pi, 100)
    ax2.plot(2.7 + 1*np.cos(theta_completo), 2 + 2*np.sin(theta_completo), 'g-', linewidth=3)
    
    ax2.plot([4.5, 4.5], [0, 4], 'g-', linewidth=3)
    ax2.plot(4.5 + 0.9*np.cos(theta), 3 + 1*np.sin(theta), 'g-', linewidth=3)
    ax2.plot(4.5 + 0.9*np.cos(theta), 1 + 1*np.sin(theta), 'g-', linewidth=3)
    
    ax2.plot([6.2, 6.2], [0, 4], 'g-', linewidth=3)
    
    ax2.plot([7, 7], [0, 4], 'g-', linewidth=3)
    ax2.plot([7, 8.5], [4, 0], 'g-', linewidth=3)
    ax2.plot([8.5, 8.5], [0, 4], 'g-', linewidth=3)
    
    ax2.set_title("Trayectoria 2D - ROBIN", fontsize=14, fontweight='bold')
    ax2.set_xlim(-1, 10)
    ax2.set_ylim(-1, 5)
    ax2.set_aspect('equal')
    ax2.grid(True, linestyle='--')

    plt.tight_layout()
    plt.show()

# Main
dibujar_nombres()

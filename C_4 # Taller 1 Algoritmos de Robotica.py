# Taller 1 Algoritmos de Robotica 
# David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
# C 4

# Importar librerias
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

#Funcion
def dibujar_vector_3d():
    print("Graficador de Vectores en 3D")
    x = float(input("Ingrese la coordenada X: "))
    y = float(input("Ingrese la coordenada Y: "))
    z = float(input("Ingrese la coordenada Z: "))
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d') # '3d' le dice a Python que añada el eje Z
    
    ax.quiver(0, 0, 0, x, y, z, color='b', arrow_length_ratio=0.1, linewidth=2, label=f'Vector ({x}, {y}, {z})')
    
    #ax.scatter(x, y, z, color='r', s=40)
    
    
    max_val = max(abs(x), abs(y), abs(z), 1) 
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])
    
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Sistema Coordenado 3D - Vector Posicion')
    ax.grid(True)
    ax.legend()
    
    plt.show()

# Main
dibujar_vector_3d()

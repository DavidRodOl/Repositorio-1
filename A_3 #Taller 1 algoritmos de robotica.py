 #Taller 1 algoritmos de robotica 
 #David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
 #A.3

#importacion de librerias 
import numpy as np

#Inicializacion de variables
x = 112
y = -77
z = 226

#Funciones 
def rectangular_a_cilindricas(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    z_cil = z
    return rho, phi, z_cil

def rectangular_a_esfericas(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

#Main 
rho, phi, z_cil = rectangular_a_cilindricas(x, y, z)
print("Coordenadas cilíndricas:\n rho:", round(rho, 2), "\n phi:", round(np.degrees(phi), 2), "\n z:", round(z_cil, 2))

r, theta, phi = rectangular_a_esfericas(x, y, z)
print("Coordenadas esfericas:\n r:", round(r, 2), "\n theta:", round(np.degrees(theta), 2), "\n phi:", round(np.degrees(phi), 2))
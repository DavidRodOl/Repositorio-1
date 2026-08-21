#Taller 1 algoritmos de robotica 
#David Alejandro Rodriguez Olaya y Robin Santigo Rojas Guzman
#A.6

import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contornos(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return imagen, contornos

def imprimir_coordenadas(contornos, nombre_logo):
    print(f"\nCoordenadas del contorno de {nombre_logo}:")
    for i, contorno in enumerate(contornos):
        print(f"Contorno {i+1}:")
        for punto in contorno:
            x, y = punto[0]
            print(f"  X: {x}, Y: {y}")

def graficar_contornos(imagen, contornos, nombre_logo):
    imagen_dibujada = imagen.copy()
    cv2.drawContours(imagen_dibujada, contornos, -1, (0, 255, 0), 2)  # verde, grosor 2
    
    imagen_rgb = cv2.cvtColor(imagen_dibujada, cv2.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imagen_rgb)
    plt.title(f"Contornos detectados - {nombre_logo}")
    plt.axis("off")
    plt.show()

# Rutas de las imágenes
ruta_logo1 = "AudiLogo.png"
ruta_logo2 = "Mazdalogo.png"

imagen1, contornos_logo1 = obtener_contornos(ruta_logo1)
imagen2, contornos_logo2 = obtener_contornos(ruta_logo2)

imprimir_coordenadas(contornos_logo1, "Audi")
imprimir_coordenadas(contornos_logo2, "Mazda")

graficar_contornos(imagen1, contornos_logo1, "Audi")
graficar_contornos(imagen2, contornos_logo2, "Mazda")
# Taller 1 Algoritmos de Robotica 
# David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
# A 6

import numpy as np

def fuerza_cilindro():
    print("Calculo de Fuerzas en Cilindro de Doble Efecto")
    
    #presion estandar de un cilindro de doble efecto = 6 bares = 600 000 Pa
    #diametros escogidos de 50 mm para el externo y 20 mm para el interno; 50mm = 0.05m ; 20mm = 0.02m

    presion = 600000.0   #Pa  
    d_embolo = 0.05     #Metros
    d_vastago = 0.02    #Metros
    
    a_embolo = (np.pi * (d_embolo ** 2)) / 4
    a_vastago = (np.pi * (d_vastago ** 2)) / 4
    a_retroceso = a_embolo - a_vastago
    
    fuerza_avance = presion * a_embolo  
    fuerza_retroceso = presion * a_retroceso    
    
    print("\nDatos del Cilindro")
    print(f"Presion configurada: {presion/100000} Bares")
    print(f"Diametro del embolo: {d_embolo*1000} Milimetros")
    print(f"Diametro del vastago: {d_vastago*1000} Milimetros")
    
    print("\nResultados del Calculo")
    print(f"Fuerza de Avance:  {fuerza_avance:.2f} N  ({fuerza_avance / 9.81:.2f} kgf)")
    print(f"Fuerza de Retroceso: {fuerza_retroceso:.2f} N  ({fuerza_retroceso / 9.81:.2f} kgf)")

# Main
fuerza_cilindro()

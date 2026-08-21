#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#B 1

#Funcion 
def datos():
    voltaje = float(input("Ingresa el voltaje del circuito (v):"))
    corriente = float(input("Ingresa la corriente del circuito (A):"))
    return voltaje, corriente

#Main 
voltaje, corriente = datos()
potencia = voltaje * corriente
print("La potencia del circuito tiene un valos de", round(potencia, 2), "watts")

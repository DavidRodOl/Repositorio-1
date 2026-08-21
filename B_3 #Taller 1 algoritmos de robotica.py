#Taller 1 Algoritmos de Robotica 
#David Alejandro Rodriguez Olaya y Robin Santiago Rojas Guzman
#B 3

#Importar librerias
import math

#Funcion 
def calculador_de_volumenes():
    while True:
        print("\nSelecciona un solido:" )
        print("1. Prisma rectangular." )
        print("2. Piramide (base cuadrada)." )
        print("3. Cono truncado." )
        print("4. Cilindro." )
        print("5. Salir." )
        
        opcion = input("Selecciona el solido (1-5): ")
        
        if opcion == "1" :
            print("Volumen del prisma\n")
            base = float(input("ingrese la base: "))
            ancho  = float(input("ingrese el ancho: "))
            altura = float(input("ingrese la altura: "))
            
            volumen = base * ancho * altura
            print(f"El volumen del prisma es: {round(volumen, 2)}")
        
        elif opcion == "2" :
            print("Volumen de la piramide\n")
            lado = float(input("ingrese el lado de la base: "))
            altura = float(input("ingrese la altura: "))
            
            volumen = (1/3) * (lado**2) * altura
            print(f"El volumen de la piramide es: {round(volumen, 2)}")
            
        elif opcion == "3" :
            print("Volumen del cono truncado\n")
            R_mayor = float(input("ingrese el radio mayor(R): "))
            r_menor = float(input("ingrese el radio menor(r: "))
            altura = float(input("ingrese la altura:"))
            
            volumen = (1/3) * math.pi * altura * (R_mayor**2 + r_menor**2 + R_mayor * r_menor)
            print(f"El volumen del cono truncado es: {round(volumen, 2)}")
            
        elif opcion == "4" :
            print("Volumen del cilindro\n")
            radio = float(input("ingrese el radio: "))
            altura = float(input("ingrese la altura: "))
            
            volumen = math.pi * (radio**2) * altura
            print(f"El volumen del cilindro es: {round(volumen, 2)}")
        
        elif opcion == "5" :
            print("Gracias por usarme jajaja\n")
            break
        
        else:
            print("opcion invalida, intente de nuevo ")
#Main 
calculador_de_volumenes()

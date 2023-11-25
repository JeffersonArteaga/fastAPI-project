#Juego de adivina el numero

import random

def adivinaUsuario():
  numGenerado = random.randint(1,20)
  numIngresado = -1
  print("La maquina ha generado un numero del 1 al 20 [1,20]\n¡Trata de adivinar cual es!")
  
  while (numIngresado != numGenerado):
    numIngresado = int(input("Ingresa el numero que crees que se genero: "))
    if (numGenerado == numIngresado):
      print("Haz acertado")
    else:
      print("Haz fallado")

    
def adivinaMaquina():
  numIngresado = int(input("Ingresa un numero del 1 al 20 [1,20] "))
  numMaquina = -1

  while (numIngresado != numMaquina):
    numMaquina = random.randint(1,20)
    print(f'Numero ingresado por el usuario: {numIngresado}\n Numero generado por la maquina: {numMaquina}')
    if (numIngresado == numMaquina):
      print("La maquina acertado")
    else:
      print("La maquina ha fallado")

def main():
  opcion = int(input("Ingresa como deseas jugar: \n1. Adivina el usuario \n2. Adivina la maquina\n"))

  if opcion == 1:
    adivinaUsuario()
  elif opcion == 2:
    adivinaMaquina()

main()
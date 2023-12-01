import random

def play(select_user):
  select_pc = random.randint(1, 3)
  options = ["Piedra", "Papel", "Tijera"]
  print(f'Escogiste: {options[select_user - 1]}')

  if (select_user == select_pc):
    print("\nEmpate")

  elif (select_user == 1):
    if (select_pc == 3):
      print("\nGanaste")
    else:
      print("\nPerdiste")

  elif (select_user == 2):
    if (select_pc == 1):
      print("\nGanaste")
    else:
      print("\nPerdiste")

  elif(select_user == 3):
    if (select_pc == 2):
      print("\nGanaste")
    else:
      ("\nPerdiste")

  print(f'La maquina escogio: {options[select_pc - 1]}')


def main():
  print("\nBienvenido al juego de piedra papel o tijera")
  control = "Esta es mi variable de control :)"
  while (len(control) > 0):
    try:
      select_user = int(input("\n1. Piedra \n2. Papel \n3. Tijera \nIngresa el numero de la opcion que deseas: "))

      if (1 <= select_user <= 3):
        play(select_user)
      else:
        print("\nOpcion invalida\n")

      control = input("\nPresione enter para salir, ingrese cualquier valor para volver a jugar: ")
    except ValueError :
      print("\nPor favor ingresa una opcion valida")
main()
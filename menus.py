from operaciones import *

#MENUS OPCIONES


def menuNum():   
  print("Menú Números:")
  print("1.Suma")
  print("2.Resta")
  print("3.Multiplicacion")
  print("4.División")
  op = int(input("Seleccione una opción: "))
  if op == 1:
    x = int(input("Número 1:"))
    y = int(input("Número 2:"))
    res = suma(x,y) 
    print("El resultado de la suma (", x ," + " , y , ") = " , res)
    input()

  elif op == 2:
    cadenas()
  elif op == 3:
    vectores()
  elif op == 4:
    matrices()
  else:
    print("Gracias por su participación!!")
    op = 0
  


#MENU PRINCIPAL
def menuPpal():   
  op = 1
  while op > 0: 
    print("Menú de opciones")
    print("1.Operaciones con números")
    print("2.Operaciones con cadenas")
    print("3.Operaciones con vectores")
    print("4.Operaciones con matrices")
    print("5.Listas")
    print("6.Pilas y Colas")
    print("7.Diccionarios")
    print("8.Ficheros")
    print("9.Salir")
    op = int(input("Seleccione una opción: "))
    if op == 1:
      menuNum()
    elif op == 2:
      cadenas()
    elif op == 3:
      vectores()
    elif op == 4:
      matrices()
    elif op == 5:
      listas()
    elif op == 6:
      pilas()
    elif op == 7:
      diccionarios()
    elif op == 8:
      ficheros()
    else:
      print("Gracias por su participación!!")
      op = 0


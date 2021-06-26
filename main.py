import numpy as np

def menu():
  while True:
    try:
      print("\nMenu de opciones para ejercicios")
      print("1. Sumatoria de columna")
      print("2. Sumatoria de fila")
      print("3. Sumatoria de diagonales")
      print("4. Multiplicar elementos columna")
      print("5. Multiplicar elementos fila")
      print("6. Multiplicar elementos diagonales")
      print("0. Salir")
      print("Ingrese una opción: ")
      op = input()
      return op
    except ValueError:
      print("Ingrese un numero entero!")

#metodo para separar digitos y guardarlos en una lista
def separadorCedula(CI):
 return list(map(int, str(CI)))

print("\tBienvenido a los ejercicios con la libreria Numpay\n")
CI = int(input('\nIngrese su número de cedula: '))
digitosCedula = separadorCedula(CI)

#aqui se crea una matriz con dimensiones 100 X 100
matriz = np.empty((100,100))

#Se introduce de manera repetida los digitos individuales de la cedula por medio de una lista
for i in range(10):
  matriz[:,i]= digitosCedula[i]
  matriz[:,i+10]= digitosCedula[i]
  matriz[:,i+20]= digitosCedula[i]
  matriz[:,i+30]= digitosCedula[i]
  matriz[:,i+40]= digitosCedula[i]
  matriz[:,i+50]= digitosCedula[i]
  matriz[:,i+60]= digitosCedula[i]
  matriz[:,i+70]= digitosCedula[i]
  matriz[:,i+80]= digitosCedula[i]
  matriz[:,i+90]= digitosCedula[i]
print(matriz)

op = 1
while(op != 0):
  op = int(menu())
  if op == 1:
    #Pide el numero de columna
    columna = int(input('\nIngrese el número de columna: '))
    #Crea un arreglo vacio de 100
    matrizColumna = np.empty(100)
    #Recoge todos los valores de la columna
    matrizColumna = matriz[:,columna-1]
    print("\nLa sumatoria de los elementos de la columna ingresada es: ")
    #Muestra la sumatoria de esa columna
    print(matrizColumna.sum())
  elif op == 2:
    #Pide el numero de fila
    fila = int(input('\nIngrese el número de fila: '))
    #Crea un arreglo vacio de 100
    matrizFila = np.empty(100)
    #Recoge todos los valores de la fila
    matrizFila = matriz[fila-1]
    print("\nLa sumatoria de los elementos de la fila ingresada es: ")
    #Muestra la sumatoria de esa fila
    print(matrizFila.sum())
  elif op == 3:
    #Mitad de la matriz
    mitadMatriz = matriz[50][50]
    #Crea dos arreglos de dimensiones 100
    matrizDiagIzDe = np.empty(100)
    matrizDiagDeIz = np.empty(100)
    #Toma la diagonal formada de izquierda a derecha
    matrizDiagIzDe = matriz.diagonal()
    #Toma la diagonal formada de derecha a izquierda
    matrizDiagDeIz = np.fliplr(matriz).diagonal()
    #Sumatoria de las diagonales y resta el valor del centro ya que se repite 2 veces
    sumaDiagonal = matrizDiagDeIz.sum() + matrizDiagIzDe.sum() - mitadMatriz
    print("\nLa sumatoria de las diagonales es: ", sumaDiagonal)
  elif op == 4:
    #Pide el numero de columna
    columna = int(input('\nIngrese el número de columna: '))
    #Crea un arreglo vacio de 100
    matrizColumna = np.empty(100)
    #Recoge todos los valores de la columna
    matrizColumna = matriz[:,columna-1]
    print("\nLa multiplicacion de los elementos de la columna ingresada es: ")
    #Muestra la multiplicacion de esa columna
    print(np.prod(matrizColumna))
  elif op == 5:
    #Pide el numero de fila
    fila = int(input('\nIngrese el número de fila: '))
    #Crea un arreglo vacio de 100
    matrizFila = np.empty(100)
    #Recoge todos los valores de la fila
    matrizFila = matriz[fila-1]
    print("\nLa multiplicacion de los elementos de la fila ingresada es: ")
    #Muestra la multiplicacon de esa fila
    print(np.prod(matrizFila))
    #La multiplicacion funciona a la perfeccion, pero por el tamaño de los numeros solo se presentara el valor 0.0 cuando el resultado sea mayor a la memoria
  elif op == 6:
    #Crea dos arreglos de dimensiones 100
    matrizDiagIzDe = np.empty(100)
    matrizDiagDeIz = np.empty(100)
    #Toma la diagonal formada de izquierda a derecha
    matrizDiagIzDe = matriz.diagonal()
    #Toma la diagonal formada de derecha a izquierda
    matrizDiagDeIz = np.fliplr(matriz).diagonal()
    #Borra uno de los valores repetido de la mitad de la matriz en cualquier de los arreglos
    np.delete(matrizDiagIzDe, 50, axis=None)
    #Multiplicacion de las diagonales
    multipliDiagonales = (np.prod(matrizDiagDeIz) * np.prod(matrizDiagIzDe)) 
    print("\nLa multiplicacion de las diagonales es: ", multipliDiagonales)
    #La multiplicacion funciona a la perfeccion, pero por el tamaño de los numeros solo se presentara el valor 0.0 cuando el resultado sea mayor a la memoria
  elif op == 0:
    print("\nElaborado por: Daniel Guachamin")
  else:
    print("\nIngrese una opcion válida")

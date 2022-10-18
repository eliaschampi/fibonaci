anterior = 0
actual = 1

suma = 0
serie = 1

hasta = int(input("Ingrese limite de la serie: "))

while serie <= hasta:
  print(suma)
  serie += 1
  anterior = actual
  actual = suma
  suma = anterior + actual
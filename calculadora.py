#Creado por fran
def add(a, b):
  return a + b
def subtract(a, b):
  return a -b
def multiply(a, b):
  return a*b
def divide(a, b):
  if b == 0:
    return 'Error: No se puede dividir por cero'
  return a/b
def exp(a, b):
  return a**b

def calculadora():
  a = float(input('Indique un valor de a: '))
  b = float(input('Indique un valor de b: '))

  print(add(a, b))
  print(subtract(a, b))
  print(multiply(a, b))
  print(divide(a, b))
  print(exp(a, b))

calculadora()
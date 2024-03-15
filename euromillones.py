#Euromillones

#euromillones
import random
numeros_normales = range(1, 51)
numeros_estrella = range(1, 13)
print(random.sample(numeros_normales, k=5)) #choice para aleatorios sin mas, sample para que no repita aleatorios
print(random.sample(numeros_estrella, k=2))

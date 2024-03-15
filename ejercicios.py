# Write code below 💖
import random
print('')
def fortune():
  cosas = ['Dont pursue happiness, create it.','All things are difficult before they are easy.',
          'The early bird gets the worm, but the second mouse gets the cheese.','Someone in your life needs a letter from you.',
          'Dont just think. Act!','Your heart will skip a beat.','The fortune you search for is in another cookie.',
          'Help! Im being held prisoner in a Chinese bakery!']
  num = random.randint(1, 8)

  print(cosas[num])

fortune()
fortune()
print('')

def happy_birthday(name):
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear ' + name )
  print('Happy birthday to you')

happy_birthday('Bicho')
print('')

def introduce_parametro_distancia():
  distance = float(input('Introduce los kilometros: '))
  return distance

def distance_to_miles(distance):
  miles = distance/1.609
  print(miles)

distance_to_miles(introduce_parametro_distancia())
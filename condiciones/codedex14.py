# Bola mágica del 🎱
#Codédex

import random

pregunta = input('Haz tu pregunta: ')

random_numero= random.randint(1, 9)
# print(random_numero)

if random_numero == 1:
  respuesta = 'Yes - definitely'
elif random_numero == 2:
  respuesta = 'It is decidedly so'
elif random_numero == 3:
  respuesta = 'Without a doubt'
elif random_numero == 4:
  respuesta = 'Reply hazy, try again'
elif random_numero == 5:
  respuesta = 'Ask again later'
elif random_numero == 6:
  respuesta = 'Better not tell you now'
elif random_numero == 7:
  respuesta = 'My sources say no'
elif random_numero == 8:
  respuesta = 'Outlook not so good'
elif random_numero == 9:
  respuesta = 'Very doubtful'
else:
  respuesta = 'Error'
  
print('pregunta:      ' + pregunta)
print('Magic 8 Ball:  ' + respuesta)

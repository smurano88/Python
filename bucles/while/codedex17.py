# Adivina número 🔢
# Codédex

numero = 0
intento = 0

while guess != 6 and tries < 5:
  guess = int(input('Di un numero  '))
  intento = intento + 1

if numero != 6:
  print('Se acabaron los intentos')
else:
  print('¡Lo tienes')

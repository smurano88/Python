# Enter PIN 🏦
# Codédex


pin = int(input('Introduce tu PIN: '))

while pin != 1234:
  pin = int(input('PIN incorrecto. Vuelve a introducir el PIN: '))

if pin == 1234:
  print('¡PIN correcto!')

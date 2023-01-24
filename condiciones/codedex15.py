# Sorting Hat 🧙‍♂️
# Codédex

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ============== Pregunta 1 ==============

print('P1) ¿Prefieres el amanecer o el anochecer?')

print('  1) Amanecer')
print('  2) Anochecer')

respuesta = int(input('Introduce tu respuesta (1-2): '))

if respuesta == 1:
  gryffindor += 1
  ravenclaw += 1
elif respuesta == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Respuesta Incorrecta.')

# ============== Pregunta 2 ==============

print("\nP2) Cuando muera, quiero que la gente me recuerde como:")

print('  1) El bueno')
print('  2) El grande')
print('  3) El sabio')
print('  4) El audaz')

respuesta = int(input('Introduce tu respuesta (1-4): '))

if respuesta == 1:
  hufflepuff += 1
elif respuesta == 2:
  slytherin +=1
elif respuesta == 3:
  ravenclaw +=1
elif respuesta == 4:
  gryffindor +=1
else:
  print('Respuesta incorrecta.')

# ============== Pregunta 3 ==============

print('\nP3) ¿Qué instrumento prefieres escuchar?')

print('  1) El violín')
print('  2) La trompeta')
print('  3) El piano')
print('  4) El tambor')

respuesta = int(input('Introduce tu respuesta (1-4): '))

if respuesta == 1:
  slytherin +=1
elif respuesta == 2:
  hufflepuff +=1
elif respuesta == 3:
  ravenclaw +=1
elif respuesta == 4:
  gryffindor +=1
else:
  print('Respuesta incorrecta.')
  
#print(gryffindor)
#print(ravenclaw)
#print(hufflepuff)
#print(slytherin)

print("\n===========================")
print("        RESULTADO:")
print("===========================\n")

<<<<<<< HEAD
#Si gryffindor es la mayor
=======
>>>>>>> a4fbf166522b853838d078ee8cc440d3996cc21f
if(gryffindor > ravenclaw and gryffindor > slytherin and gryffindor > hufflepuff):
    print("🦁 Gryffindor\n")
#sino si ravenclaw es la mayor
elif(ravenclaw > gryffindor and ravenclaw > slytherin and ravenclaw > hufflepuff):
    print("🦅 Ravenclaw\n")
#sino si slytherin es la mayor
elif(slytherin > ravenclaw and slytherin > gryffindor and slytherin > hufflepuff):
    print("🦡 Slytherin\n")
#sino si hufflepuff es la mayor
elif(hufflepuff > ravenclaw and hufflepuff > gryffindor and hufflepuff > slytherin):
    print("🐍 Hufflepuff")
else:
<<<<<<< HEAD
#Se han producido empates
=======

>>>>>>> a4fbf166522b853838d078ee8cc440d3996cc21f
    print("*****  VARIAS CASAS ******\n")
    print("---------------------------")
    print("Desglosado:\n")
    print("🦁 Gryffindor = ",gryffindor)
    print("🦅 Ravenclaw = ",ravenclaw)
    print("🦡 Slytherin = ",slytherin)
    print("🐍 Hufflepuff = ",hufflepuff)
    print("---------------------------")

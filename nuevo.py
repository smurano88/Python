datos = [1,2,3,4,5]
print(datos[0])

datos2 = []

for i in range (0,4):
    valor = int((input("Dame un valor {}: ".format(i) )))
    datos2.append(valor)

for i in range(3,-1,-1):
    print(datos2[i])

lista = []
for i in range (0,3):

    lista.append(int(input("Dame un número {}: ".format(i))))

for x in lista:
    print(x)
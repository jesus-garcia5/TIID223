#Declarando un arreglo bien
numeros=[10,20,30,40,50]
print(numeros[2])
"""
#imprime la pos. 30
print(numeros[2])

#Reasigna un nuevo valor
numeros[3]=15
print(numeros)

#Agregamos un nuevo valor al arreglo
numeros.append(60)
print(numeros)"""

#Eliminamos por pos.
numeros.pop(1)
print(numeros)

#Eliminamos por valor 
numeros.remove(30)
print(numeros)

frutas=["mango","manzana", "uva","pera","maracuya"]

frutas.remove("uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("kiwi")
print(frutas)
frutas[2]="fresa"
print(frutas)

arreglo=[]
n = int(input("ingresa el tamaño del arreglo: "))
arreglo[0]=int(input("ingresa el valor 0"))
print(arreglo)
secuencia = int(input('indique hasta que numero quiere ver la secuencia de Fibonacci: '))
n1 = 0
n2 = 1
contador = 0
print('Secuencia de Fibonacci hasta:', secuencia)
print(n1)
print(n2)
while contador < secuencia:
    n1 = n2
    n2 = contador
    contador = n1 + n2

print(contador)

'''
# la secuencia de Fibonacci parte de dos valores iniciales que dan pie al comienzo de la secuencia: 0 y 1:
secuencia = int(input('indique hasta que numero quiere ver la secuencia de Fibonacci: '))
n1 = 0
n2 = 1
# cada ciclo va a sumar el valor de los dos numeros anteriores hasta el infinito: 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 + 2 = 5 [...] dando como resultado una scuencia así: 0, 1, 1, 2, 3, 5, 8 [...]
# ese resultado va a ser el conteo: 
contador = 0
print('Secuencia de Fibonacci hasta:', secuencia)
print(n1)
print(n2)
# hay que establecer la condicion del bucle. En este caso debe repetirse hasta llegar al valor de la 'secuencia':
while contador < secuencia: # esto significa que el programa va a seguir corriendo mientras que sea menor que la variable 'secuencia'. Una vez sea mayor, el programa para.
    n1 = n2 # aqui la secuencia se desplaza hacia la derecha con lo que 'n1' que antes valia 0 pasa a valer 1, o lo que valia antes 'n2' 
    n2 = contador # seguimos desplazando la secuencia a la derecha y otorgamos el valor de 'n2' a al contador. 
    contador = n1 + n2 # esto es: 0 + 1 = 1
    print(contador)
'''
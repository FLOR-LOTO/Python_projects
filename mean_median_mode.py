"""
La 'mean' es el valor promedio de todos los valores de un conjunto de datos
"""
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

mean = sum(list1) / len(list1)

print(mean)

"""
La 'median' es el valor medio entre todos los valores ordenados. Aquí necesitamos calcular el valor medio de todos los valores de un conjunto de datos. 
El código calcula la mediana de una lista de números. Si la lista tiene un número par de elementos, la mediana es el promedio de los dos valores centrales. Si la lista tiene un número impar de elementos, la mediana es el valor central.
El operador // redondea la division al entero mas cercano inferior, se usa para realizar divisiones enteras, lo que es útil para encontrar la posición del elemento central cuando se calcula la mediana de una lista.
"""
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort() # [12, 12, 16, 20, 20, 20, 23, 24, 25, 30]

#si la cantidad de elemento es par:
if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2] #calcula la posición del elemento central superior (en este caso, es posicion 5)
    m2 = list1[len(list1)//2 - 1] #calcula la posición del elemento central superior -1 (en este caso, es posicion 4)
    median = (m1 + m2)/2 #La mediana se calcula como el promedio de estos dos valores: (20 + 20) / 2 = 20.0.
#si la cantidad de elemento es impar:
else:
    median = list1[len(list1)//2]
print(median)

"""
La 'mode' es el valor que aparece con más frecuencia entre todos los valores.
"""
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}

for i in list1: #recorre cadsa elemento
    frequency.setdefault(i, 0) #asegura que cada número esté en el diccionario frequency con un valor inicial de 0 si no está presente.
    frequency[i]+=1 #incrementa la cuenta de la frecuencia del número i en 1
    #{12: 2, 16: 1, 20: 3, 30: 1, 25: 1, 23: 1, 24: 1}

frequent = max(frequency.values()) #frequency.values() devuelve una vista de todos los valores en el diccionario frequency, max(frequency.values()) encuentra el valor máximo en esta vista, que es la frecuencia más alta.

#El bucle for recorre cada par clave-valor (i, j) en el diccionario frequency.
for i, j in frequency.items(): #frequency.items() devuelve una vista de pares clave-valor.
    if j == frequent: #Si el valor j (la frecuencia) es igual a frequent (la frecuencia máxima), entonces i (el número clave) es asignado a mode.
        mode = i
print(mode)
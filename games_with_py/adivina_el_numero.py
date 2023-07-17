#Adivinando el número del usuario

import random
intentos_realizados = 0

print("Hola, ¿cómo te llamas?")
name = input()

number = random.randint(1,20)
print("Bueno, " + name + ", estoy pensando en un número entre 1 y 20")

while intentos_realizados < 5:
    print("Adivina el número")
    intento = input()
    intento = int(intento)

    intentos_realizados += 1

    if intento < number :
        print("El número es muy pequeño")
    if intento > number :
        print("El número es muy grande")
    if intento == number :
        break

if intento == number :
    intentos_realizados = str(intentos_realizados)
    print("Genial, " + name + ", lograste adivinar el número en " + intentos_realizados + " intentos")

if intento != number :
    number = str(number)
    print("No lo adivinaste. El número " + number + " es en el que pensaba")
import random

def generar_numero_secreto(largo_numero):
    numeros = list(range(10))
    random.shuffle(numeros)
    num_secreto = ''

    for i in range(largo_numero):
        num_secreto += str(numeros[i])
    return num_secreto

def obtener_puntos_fijos(num_usuario, num_secreto):
    if num_usuario == num_secreto:
        return '''
░░░█▀█░█▀▄░▀█▀░█░█░▀█▀░█▀█░█▀█░█▀▀░▀█▀░█▀▀░░░█░█
░░░█▀█░█░█░░█░░▀▄▀░░█░░█░█░█▀█░▀▀█░░█░░█▀▀░░░▀░▀
░░░▀░▀░▀▀░░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀░▀'''
    
    pista = []

    for i in range(len(num_usuario)):
        if num_usuario[i] == num_secreto[i]:
            pista.append('fijo')
        elif num_usuario[i] in num_secreto:
            pista.append('punto')
    
    if len(pista) == 0:
        return 'tablas'
    
    pista.sort()

    return ' '.join(pista)

def solo_num(num):
    error = 'Ingrese un número válido: solo números, %s dígitos, sin repetición'%(largo_numero)
    #comprueba si lo ingresado por el usuario son solo numeros válidos
    if num == '':
        print(error)
        return False
    #Evaluación si tiene la longitud adecuada
    for i in num:
        #Evalación si el digito es un número
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            print(error)
            return False
        #Evaluación si tiene números repetidos
        if num.count(i) > 1:
            print(error)
            return False     
    return True

def jugar_de_nuevo():
    #Devuelve True si el usuario quiere jugar de nuevo
    print()
    print('¿Quieres jugar de nuevo? (si ó no):')
    return input().lower().startswith('s')

#implementación del juego
#variables iniciales
while True:
        print()
        largo_numero = input('Elige el tamaño del número a adivinar: ')
        max_intentos = input('¿Cuántos intentos quieres?: ')

        try:
            largo_numero = int(largo_numero)
            max_intentos = int(max_intentos)
        except:
            print('Ingrese dígitos válidos (solo números)')
            continue
        break 
    
print()
print('---')
print()
print('El número es de %s dígitos.'%(largo_numero))
print('La nomenclatura de las pistas es la siguiente:')
print()
print('Palabra:         Significado:')
print('Fijo             Un dígito correcto en la posición correcta')
print('Punto            Un dígito correcto en la posición incorrecta')
print('Tablas           Ningún dígito correcto :/')
print()

#juego

while True:
    #generación número secreto
    num_secreto = generar_numero_secreto(largo_numero)
    print('Tengo un número en me...moria. Tienes %s intentos para adivinarlo.' %(max_intentos))
    
    #imput usuario
    num_intento = 1
    while num_intento <= max_intentos:
        num_usuario = ''
        while len(num_usuario) != largo_numero or not solo_num(num_usuario):
            print()
            print('Intento N°%s'%(num_intento))
            num_usuario = input()
        
        puntos_fijos = obtener_puntos_fijos(num_usuario, num_secreto)
        print(puntos_fijos)
        num_intento += 1
    
    #comprobación número usuario
        if num_usuario == num_secreto:
            break
        if num_intento > max_intentos:
            print()
            print('Te quedaste sin intentos. La respuesta era %s.'%(num_secreto))

    if not jugar_de_nuevo():
        break

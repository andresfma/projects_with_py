import random
imagen_ahorcado = ['''

    +---+
    |   |
        |
        |
        |
        |
 =========''','''   

     +---+
    |   |
    0   |
        |
        |
        |
 =========''','''   

     +---+
    |   |
    0   |
    |   |
        |
        |
 =========''','''   

     +---+
    |   |
    0   |
   /|   |
        |
        |
 =========''','''   

     +---+
    |   |
    0   |
   /|\  |
        |
        |
 =========''','''   

     +---+
    |   |
    0   |
   /|\  |
   /    |
        |
 =========''','''   

     +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
 =========''','''   

     +---+
    |   |
   [0   |
   /|\  |
   / \  |
        |
 =========''','''   

     +---+
    |   |
   [0]  |
   /|\  |
   / \  |
        |
 =========''']

palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide pentagono hexagono heptagono octogono'.split(),'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(), 'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def obtener_palabra_al_azar(diccionario_de_palabras):
    clave_palabras = random.choice(list(diccionario_de_palabras.keys()))
    indice_de_palabras = random.randint(0, len(diccionario_de_palabras[clave_palabras])-1)
    return [diccionario_de_palabras[clave_palabras][indice_de_palabras], clave_palabras]

def mostrar_tablero(imagen_ahorcado, letras_incorrectas, letras_correctas, palabra_secreta):
    print(imagen_ahorcado[len(letras_incorrectas)])
    print()

    print('Letras incorrectas:', end='')
    for letra in letras_incorrectas:
        print(letra, end='')
    print()

    espacios_vacios = '_' * len(palabra_secreta)

    for i in range(len(palabra_secreta)): #mostrar los espacios vacios con la letras correctas
        if palabra_secreta[i] in letras_correctas:
            espacios_vacios = espacios_vacios[:i] + palabra_secreta[i] + espacios_vacios[i+1:]
    
    for letra in espacios_vacios: #espacios entre letras de la palabra secreta
        print(letra, end='')
    print()

def obtener_intento(letras_probadas): #verificación de la letra ingresada
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Introduzca solo una letra')
        elif intento in letras_probadas:
            print('Esta letra ya ha sido probada :/')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Ingrese una LETRA ;)')
        else:
            return intento

def jugar_de_nuevo():
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

#inicio implementación del juego

print('A H O R C A D O')
letras_incorrectas = ''
letras_correctas = ''
palabra_secreta, clave_secreta = obtener_palabra_al_azar(palabras)
juega_terminado = False

while True:
    print('La palabra secreta está dentro del grupo de las "' + clave_secreta + '".')
    mostrar_tablero(imagen_ahorcado, letras_incorrectas, letras_correctas, palabra_secreta)
    intento = obtener_intento(letras_correctas + letras_incorrectas)

    if intento in palabra_secreta:
        letras_correctas = letras_correctas + intento

        #verificación de si el jugador ya gano
        encontrando_todas_letras = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_correctas:
                encontrando_todas_letras = False
                break
        if encontrando_todas_letras:
            print('Genial, la palabra secreta es "' + palabra_secreta + '"!. Ganaste!')
            juega_terminado = True
    else:
        letras_incorrectas = letras_incorrectas + intento

        if len(letras_incorrectas) == len(imagen_ahorcado)-1:
            mostrar_tablero(imagen_ahorcado, letras_incorrectas, letras_correctas, palabra_secreta)
            print('Te has quedado sin intentos :(\nDespués de ' + str(len(letras_incorrectas)) + ' intentos fallidos y ' + str(len(letras_correctas)) + ' aciertos, la palabra era "' + palabra_secreta + '".')
            print('GAME OVER')
            juega_terminado = True
    
    #repetir juego?
    if juega_terminado:
        if jugar_de_nuevo():
            letras_incorrectas = ''
            letras_correctas = ''
            juega_terminado = False
            palabra_secreta, clave_secreta = obtener_palabra_al_azar(palabras)
        else:
            break

    

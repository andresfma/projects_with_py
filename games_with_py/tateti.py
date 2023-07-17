import random

def dibujar_tablero(tablero):
    print('     |     |')
    print('  ' + tablero[7] + '  |  ' +  tablero[8] + '  |  ' + tablero[9])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + tablero[4] + '  |  ' +  tablero[5] + '  |  ' + tablero[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + tablero[1] + '  |  ' +  tablero[2] + '  |  ' + tablero[3])
    print('     |     |')

def ingresa_letra_jugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()

    #El primer elemento dentro de las siguientes lista será el jugador el segundo la compu
    if letra == 'X':
        return['X','O']
    else:
        return['O','X']
    
def quien_comienza():
    if random.randint(0,1) == 0:
        return 'La compu ;)'
    else:
        return 'Tú, magnate ;)'

def jugar_de_nuevo():
    print('¿Deseas jugar de nuevo? si o no')
    return input().lower().startswith('s')

def hacer_jugada(tablero, letra, jugada):
    tablero[jugada] = letra

def ganador(ta, le):
    #retorna True si se hace un 3 en raya
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or (ta[1] == le and ta[2] == le and ta[3] == le) or (ta[4] == le and ta[5] == le and ta[6] == le) or (ta[1] == le and ta[4] == le and ta[7] == le) or (ta[2] == le and ta[5] == le and ta[8] == le) or (ta[3] == le and ta[6] == le and ta[9] == le) or (ta[3] == le and ta[5] == le and ta[7] == le) or (ta[1] == le and ta[5] == le and ta[9] == le))

def obtener_duplicado_tablero(tablero):
    dup_tablero = []

    for i in tablero:
        dup_tablero.append(i)
    
    return dup_tablero

def espacio_libre(tablero, jugada):
    #retorna True si existe aún un espacio libre para jugar
    return tablero[jugada] == ' '

def obtener_jugada_jugador(tablero):
    jugada = ''
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not espacio_libre(tablero, int(jugada)):
        print('¿Cúal es tu proxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegir_azar_de_lista(tablero, lista_jugada):
    jugadas_posibles = []
    for i in lista_jugada:
        if espacio_libre(tablero, i):
            jugadas_posibles.append(i)
    
    if len(jugadas_posibles) != 0:
        return random.choice(jugadas_posibles)
    else:
        return None
    
def obtener_jugada_compu(tablero, letra_compu):
    if letra_compu == 'X':
        letra_jugador = 'O'
    else:
        letra_jugador = 'X'
    
    #implementación de la IA  para hacer una jugada coherente
    #verificar si puede ganar
    for i in range(1,10):
        copia = obtener_duplicado_tablero(tablero)
        if espacio_libre(copia, i):
            hacer_jugada(copia, letra_compu, i)
            if ganador(copia, letra_compu):
                return i
    
    #bloqueo por parte de la IA cuando el jugador puede ganar

    for i in range(1,10):
        copia = obtener_duplicado_tablero(tablero)
        if espacio_libre(copia, i):
            hacer_jugada(copia, letra_jugador, i)
            if ganador(copia, letra_jugador):
                return i
            
    #intentar ocupar esquinas si estan libres
    jugada = elegir_azar_de_lista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    
    #intentar ocupar el centro si esta libre
    if espacio_libre(tablero, 5):
        return 5
    
    #ocupar alguno de los lados
    return elegir_azar_de_lista(tablero, [2, 4, 6, 8])

def tablero_completo(tablero):
    for i in range(1,10):
        if espacio_libre(tablero, i):
            return False
    return True

#Iniciando programa

print('T a  T e  T i')

while True:
    #reset del tablero
    el_tablero = [' ']*10
    letra_jugador, letra_compu = ingresa_letra_jugador()
    turno = quien_comienza()
    print(turno + ' irás primero')
    juego_en_curso = True

    while juego_en_curso:
        if turno == 'Tú, magnate ;)':
            #turno del jugador
            dibujar_tablero(el_tablero)
            jugada = obtener_jugada_jugador(el_tablero)
            hacer_jugada(el_tablero, letra_jugador, jugada)

            if ganador(el_tablero, letra_jugador):
                dibujar_tablero(el_tablero)
                print('¡ ¡ Y O U    W I N ! !')
                juego_en_curso = False
            else:
                if tablero_completo(el_tablero):
                    dibujar_tablero(el_tablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'La compu ;)'
        
        else:
            #turno computadora
            jugada = obtener_jugada_compu(el_tablero, letra_compu)
            hacer_jugada(el_tablero, letra_compu, jugada)

            if ganador(el_tablero, letra_compu):
                dibujar_tablero(el_tablero)
                print('Y O U    L O S E')
                juego_en_curso = False
            else:
                if tablero_completo(el_tablero):
                    dibujar_tablero(el_tablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'Tú, magnate ;)'
    if not jugar_de_nuevo():
        break


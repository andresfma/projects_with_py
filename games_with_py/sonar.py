import random
import sys

def dibujar_tablero(tablero):
    linea_hor = '   '
    for i in range(1, 6):
        linea_hor += (' ' * 9) + str(i)
    #numeros superiores
    print(linea_hor)
    print('    ' + ('0123456789' * 6))
    print()

    #filas
    #los numeros menores a 10 requieren de un espacio adicional
    for i in range(15):
        if i < 10:
            espacio_extra = ' '
        else:
            espacio_extra = ''
        print('%s%s %s %s' % (espacio_extra, i , obtener_fila(tablero, i), i))

    #imprimir los numeros a lo largo del borde inferior
    print()
    print('    ' + ('0123456789' * 6))
    print(linea_hor)

def obtener_fila(tablero, fila):
    #estructura de dato de un tablero según la fila
    fila_tablero = ''
    for i in range(60):
        fila_tablero += tablero[i][fila]
    return fila_tablero

def obtener_nuevo_tablero():
    #estructura de datos para un tablero de 60*15
    tablero = []
    for x in range(60):
        tablero.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')
    return tablero

def obtener_cofres(num_cofres):
    #estructua de datos de cofres, lista(cofre1(x,y, cofre2(x,y)))
    cofres = []
    for i in range(num_cofres):
        cofres.append([random.randint(0, 59), random.randint(0, 14)])
        return cofres

def movimiento_valido(x, y):
    #devuelve True si el moviento del usuario esta dentro de las coordenadas
    return x >= 0 and x <=59 and y >= 0 and y <= 14

def realizar_movimiento(tablero, cofres, x, y):
    #cambia el tablero mostrando un número del radar,
    #devuelve False si la jugada no es válida
    #Elimina el cofre de la lista si lo encuentra
    
    if not movimiento_valido(x, y):
        return False
    
    menor_distancia = 100 #distancia  entre cofres menor de 100

    for cx, cy in cofres:
        if abs(cx - x) > abs(cy - y):
            distancia = abs(cx - x)
        else:
            distancia = abs(cy - y)
        
        if distancia < menor_distancia:
            menor_distancia = distancia #buscando el cofre más cercano
        
        if menor_distancia == 0:
            #x,y coinciden con un cofre
            tablero.remove([x, y])
            return 'Encontraste un cofre, ¡¡ bien hecho !!'
        else:
            if menor_distancia < 10:
                tablero[x][y] = str(menor_distancia)
                return 'Tesoro detectado a una distancia %s del sonar.' %(menor_distancia)
            else:
                tablero[x][y] = '0'
                return 'El sonar no ha detectado nada. Todos los cofres estan fuera de rango'

def ingresar_movimiento():
    print('Ingresa las coordenadas deseadas. x(0-59), y(0-14) (o teclea salir)')
    while True:
        movimiento = input()
        if movimiento.lower() == 'salir':
            print('Te has rendido. Mejor suerte la próxima')
            sys.exit()
        
        movimiento = movimiento.split()
        if len(movimiento) == 2 and movimiento[0].isdigit() and movimiento[1].isdigit() and movimiento_valido(int(movimiento[0], int(movimiento[1]))):
            return [int(movimiento[0]), int(movimiento[1])]
        print('Ingresa un número de 0 a 59, un espacio, y luego un número de 0 a 14')

def jugar_de_nuevo():
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

def mostrar_instrucciones():
    print('''Instrucciones:
Eres el Simón, un buque cazador de tesoros. Tu misión actual
es encontrarlos tres cofres con tesoros perdidos que se hallan ocultos en
la parte del océano en que te encuentras y recogerlos.
Para jugar, ingresa las coordenadas del punto del océano en que quieres
colocar un dispositivo sonar. El sonar puede detectar cuál es la distancia 
al cofre más cercano.
Por ejemplo, la d abajo indica dónde se ha colocado el dispositivo, y los 
números 2 representan los sitios a una distancia 2 del dispositivo. Los
números 4 representan los sitios a una distancia 4 del dispositivo.
           
            444444444
            4       4
            4 22222 4
            4 2   2 4
            4 2 d 2 4
            4 2   2 4
            4 22222 4
            4       4
            444444444

Pulsa enter para continuar...''')
    input()

    print('''Por ejemplo, aquí hay un cofre del tesoro (la c) ubicado a una distancia
2 del dispositivo sonar (la d):

              22222
              c   2
              2 d 2
              2   2
              22222
El punto donde el dispositivo fue colocado se indicará con una d.

Los cofres del tesoro no se mueven. Los dispositivos sonar pueden detectar
cofres hasta una distancia 9. Si todos los cofres están fuera del alcance, 
el punto se indicará con un O.

Si un dispositivo es colocado directamente sobre un cofre del tesoro, has
descubierto la ubicación del cofre, y este será recogido. El dispositivo 
sonar permanecerá allí.

Cuando recojas un cofre, todos los dispositivos sonar se actualizarán para 
localizar el próximo cofre hundido más cercano.
Pulsa enter para continuar...''')
    input()
    print()

#iniciando el juego
print(' S O N A R')
print()
print('¿Te gustaría ver las largas instrucciones? (si/no)')
if input().lower().startswith('s'):
    mostrar_instrucciones()

while True:
    num_sonar = 16
    tablero = obtener_nuevo_tablero()
    cofres = obtener_cofres(3)
    dibujar_tablero(tablero)
    movimientos_previos = []

    while num_sonar > 0:
        #comienzo de un turno:

        #estado de sonares/cofres
        if num_sonar > 1: extra_sonar = 's'
        else: extra_sonar = ''
        if len(cofres) > 1: extra_cofre = 's'
        else: extra_cofre = ''
        print('Aún tienes %s dispositivo%s sonar. Falta encontrar %s cofre%s' %(num_sonar, extra_sonar, len(cofres), extra_cofre))

        x, y = ingresar_movimiento()
        movimientos_previos.append([x, y])

        resultado_movimiento = realizar_movimiento(tablero, cofres, x, y)
        if resultado_movimiento == False:
            continue
        else:
            if resultado_movimiento == 'Encontraste un cofre, ¡¡ bien hecho !!':
                #actualización de los sonares en el mapa
                for x, y in movimientos_previos:
                    realizar_movimiento(tablero, cofres, x, y)
            dibujar_tablero(tablero)
            print(resultado_movimiento)
        if len(cofres) == 0:
            print('Encontraste todos los cofres, GG')
            break
        
        num_sonar -= 1
    
    if num_sonar == 0:
        print('Te quedaste sin sonares capitán, suerte la próxima')
        print()
        print('Los cofre restantes estaban aquí:')
        for x, y in cofres:
            print('     %s, %s' %(x, y))
    
    if not jugar_de_nuevo():
        sys.exit()
# mi_diccionario = {'name':'andres', 'lastname':'mercado andrade'.split(), 'age':'21'}
# key = list(mi_diccionario.keys())[1]

# print(list(mi_diccionario))
# print(list(mi_diccionario.keys()))
# print(list(mi_diccionario.values()))
result, value_key = [mi_diccionario['lastname'][1], key]
print(value_key)

def obtener_nuevo_tablero():
    #crea un tablero vacío
    tablero = []
    for i in range(8):
        tablero.append([' ']*8)

    return tablero

print(obtener_nuevo_tablero())



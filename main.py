# Árboles con Listas Anidadas.
# lista de Números
def contar_elementos(lst):
    return len(lst)


def tiene_tres_elementos(lst):
    return contar_elementos(lst) == 3
# [ 50, 
#     [30, [], []],
#     [70, [], []]
# ]


lista = []

    

while True:
    cantidad_nodos = 0
    grado = 0

    opcion = int(input('Ingrese un valor por favor: '))
    if len(lista) == 0:
        lista.append(opcion)
        grado += 1

    else:
        if len(lista) <= 2:
            lista.append([opcion])
        else:
            print(lista)

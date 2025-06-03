# Aca lo que hacemos es crear el arbol, de manera que tenga la apariencia y comportamiento
# que esperamos: 
#        NI = Nodo Izq,              ND = Nodo Der

#                [ valor , [] ,  [] ]
#                   raíz , NI ,  ND

def crear_arbol(valor):
    return [valor, [], []]  


# Me rompió la cabeza esta, pero se pudo.
# Primero preguntamos si existe el árbol en cuestion.
# posteriormente consultamos si el valor que pasamos como argumento es menor que la raíz
# Si es menor que la raíz, tomaremos posesión del NI.
# Caso contrario reutilizamos la funcion 'crear_arbol(valor)' porq quiere decir que no hay hijo, lo que significa que creamos un subArbol

# Caso en el que el valor, sea mayor a la raíz repetimos el proceso pero esta vez hacia el ND, que es el mayor.. 

def insertar_nodo(arbol, valor):
    if not arbol:
        return crear_arbol(valor)

    if valor < arbol[0]:
        if arbol[1]:
            insertar_nodo(arbol[1],valor)
        else:
            arbol[1] = crear_arbol(valor)
    else:
        if arbol[2]:
            insertar_nodo(arbol[2],valor)
        else:
            arbol[2] = crear_arbol(valor)
    return arbol

# saque ideas desde el word que dejo la catedra para hacer el trabajo. 

def buscar_valor(arbol, valor):
    if not arbol:
        return False
    
    if valor == arbol[0]:
        return True
    elif valor < arbol[0]:
        return buscar_valor(arbol[1], valor)
    else:
        return buscar_valor(arbol[2], valor)
    

def recorrido_inorden(arbol):

    if arbol:
        recorrido_inorden(arbol[1] )  
        print(arbol[0], end = ' ' )    
        recorrido_inorden(arbol[2] )  


def recorrido_preorden(arbol):
    if arbol:
        print(arbol[0], end= ' ')
        recorrido_preorden(arbol[1])
        recorrido_preorden(arbol[2])


def recorrido_postorden(arbol):

    if arbol:
        recorrido_postorden(arbol[1])
        recorrido_postorden(arbol[2])
        print(arbol[0], end= ' ')


def contar_nodos(arbol):
    
    if not arbol:
        return 0
    
    return 1 + contar_nodos(arbol[1]) + contar_nodos(arbol[2])


def altura_arbol(arbol):

    if not arbol:
        return 0
    return 1 + max(altura_arbol(arbol[1]), altura_arbol(arbol[2]))


def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)
        print(" - " * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)

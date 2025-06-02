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
            insertar_nodo(arbol[1], valor)
        else:
            arbol[1] = crear_arbol(valor)
    else:
        if arbol[2]:
            insertar_nodo(arbol[2], valor)
        else:
            arbol[2] = crear_arbol(valor)
    return arbol

# saque ideas desde el word que dejo la catedra para hacer el trabajo. 
#


def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)
        print(" - " * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)

#--------------------------------------------------------------------------#


#Ejemplo de uso: 

# Obtendremos una lista de numeros con valores aleatorios.
lista_numeros = [50,30,60,35,65,77,66,63,70,80,20,40,15]

arbol = crear_arbol(lista_numeros[0])

# Ahora insertaremos los valores al arbol recorriendo la lista 
# esto lo hacemos recorriendo la lista desde la poscion 1, hasta el final. Ya que el primer valor fue asignado para la raíz.

for num in lista_numeros[1:]:
    insertar_nodo(arbol, num)

# Finalmente, imprimos la vista del arbol con la funcion imprimir_arbol

imprimir_arbol(arbol)



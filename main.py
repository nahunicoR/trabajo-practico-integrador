# Prueba y muestra de ejecución para el código bien modularizado y estructurado
from arbol_binario_listas import *

print('\n*-------- CREACIÓN DEL ÁRBOL --------*')
lista_numeros = [50, 30, 60, 35, 65, 77, 66, 63, 70, 80, 20, 40, 15]
print(f'Números a insertar: {lista_numeros}')

# Crear el árbol con el primer elemento
arbol = crear_arbol(lista_numeros[0])

# Insertar el resto de números
for num in lista_numeros[1:]:
    insertar_nodo(arbol, num)

print('\n*-------- VISUALIZACIÓN DEL ÁRBOL --------*')
imprimir_arbol(arbol)

print('\n*-------- INFORMACIÓN DEL ÁRBOL --------*')
print(f'Total de nodos: {contar_nodos(arbol)}')
print(f'Altura: {altura_arbol(arbol)}')

print('\n*-------- RECORRIDOS --------*')

print('Inorden (ordenado): ')
recorrido_inorden(arbol)

print('\nPreorden: ')
recorrido_preorden(arbol)

print('\nPostorden: ')
recorrido_postorden(arbol)


print('\n\n*-------- BÚSQUEDAS --------*')

valores_buscar = [35, 100, 15, 45]
for valor in valores_buscar:
    encontrado = buscar_valor(arbol, valor)
    if encontrado:
        print(f'El valor: {valor}, FUE encontrado')
    else:
        print(f'El valor: {valor}, NO ha sido encontrado en el árbol...')

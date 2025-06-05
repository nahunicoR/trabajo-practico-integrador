# trabajo-practico-integrador


## Video de Youtube

[\[Enlace del Video](https://youtu.be/Ez5TY70sx7k)]

## Presentación

[[Enlace de la presentación](https://prezi.com/p/ezyufcthspon/?present=1)]

## Documentación

[[Enlace a la documentación](https://drive.google.com/file/d/1V9KKQvWV3ENnm8CmsWUrwyFwY-Wk4pxE/view)]


Este proyecto implementa un árbol binario en Python.

## Descripción

Este proyecto presenta una implementación de un árbol binario desarrollado en Python. El código se organiza en dos archivos clave, cada uno con un rol específico dentro de la estructura general del proyecto.

*   `arbol_binario_listas.py`: Contiene la implementación del árbol binario utilizando listas.
*   `main.py`: Contiene un ejemplo de uso del árbol binario.

## Funcionalidades

El árbol binario implementa las siguientes funcionalidades:

*   Creación de un árbol binario.
*   Inserción de nodos en el árbol binario.
*   Búsqueda de valores en el árbol binario.
*   Recorrido del árbol binario en inorden, preorden y postorden.
*   Cálculo del número de nodos del árbol binario.
*   Cálculo de la altura del árbol binario.
*   Impresión del árbol binario.

## Uso

Para utilizar el árbol binario, se puede ejecutar el archivo `main.py`. Este archivo crea un árbol binario, inserta nodos, imprime el árbol, obtiene información del árbol, realiza recorridos y busca valores en el árbol.

## Estructura del código

### `arbol_binario_listas.py`

Este archivo contiene las siguientes funciones:

*   `crear_arbol(valor)`: Crea un árbol binario con el valor especificado como raíz.
*   `insertar_nodo(arbol, valor)`: Inserta un nodo con el valor especificado en el árbol binario.
*   `buscar_valor(arbol, valor)`: Busca un valor en el árbol binario.
*   `recorrido_inorden(arbol)`: Realiza un recorrido inorden del árbol binario.
*   `recorrido_preorden(arbol)`: Realiza un recorrido preorden del árbol binario.
*   `recorrido_postorden(arbol)`: Realiza un recorrido postorden del árbol binario.
*   `contar_nodos(arbol)`: Calcula el número de nodos del árbol binario.
*   `altura_arbol(arbol)`: Calcula la altura del árbol binario.
*   `imprimir_arbol(arbol, nivel=0)`: Imprime el árbol binario.

### `main.py`

Este archivo contiene el siguiente código:

```python
# Prueba y muestra de ejecución para el código bien modularizado y estructurado
from arbol_binario_listas import *

print('\\n*-------- CREACIÓN DEL ÁRBOL --------*')
lista_numeros = [50, 30, 60, 35, 65, 77, 66, 63, 70, 80, 20, 40, 15]
print(f'Números a insertar: {lista_numeros}')

# Crear el árbol con el primer elemento
arbol = crear_arbol(lista_numeros[0])

# Insertar el resto de números
for num in lista_numeros[1:]:
    insertar_nodo(arbol, num)

print('\\n*-------- VISUALIZACIÓN DEL ÁRBOL --------*')
imprimir_arbol(arbol)

print('\\n*-------- INFORMACIÓN DEL ÁRBOL --------*')
print(f'Total de nodos: {contar_nodos(arbol)}')
print(f'Altura: {altura_arbol(arbol)}')

print('\\n*-------- RECORRIDOS --------*')

print('Inorden (ordenado): ')
recorrido_inorden(arbol)

print('\\nPreorden: ')
recorrido_preorden(arbol)

print('\\nPostorden: ')
recorrido_postorden(arbol)


print('\\n\\n*-------- BÚSQUEDAS --------*')

valores_buscar = [35, 100, 15, 45]
for valor in valores_buscar:
    encontrado = buscar_valor(arbol, valor)
    if encontrado:
        print(f'El valor: {valor}, FUE encontrado')
    else:
        print(f'El valor: {valor}, NO ha sido encontrado en el árbol...')

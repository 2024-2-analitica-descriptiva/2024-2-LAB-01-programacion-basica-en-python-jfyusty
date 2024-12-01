"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide por tabulaciones.
    letter = parts[0]   # Extrae el primer elemento (index 0) de la linea.
    elements_col4 = len(parts[3].split(','))  # Cantidad de elementos en columna 4 (index 3) en cada linea.
    elements_col5 = len(parts[4].split(','))  # Cantidad de elementos en columna 5 (index 4) en cada linea
    return (letter, elements_col4, elements_col5)   # Retorna una tupla donde el primer elemento es el extraído en "letter" y el segundo y tercer elemento es la cantidad de elementos de la columna 4 y 5 respectivamente.


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.append(map_function(line))  # Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
    
    return mapped_data   # Retorna la lista de "mapped_data".


# Llamar a la función y obtener los resultados
conteo_elementos_letra = pregunta_10()
print(conteo_elementos_letra)

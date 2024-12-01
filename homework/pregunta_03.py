"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide por tabulaciones.
    letter = parts[0]   # Extrae el primer elemento (index 0)
    count = int(parts[1])   # Extrae el segundo elemento (index 1)
    return (letter, count)   # Retorna una tupla donde el primer elemento es el extraído en "letter" y el segundo elemento es el entero "count".


# Definición de la función `reduce_function` que acepta como argumento `mapped_data`, una lista de tuplas.
def reduce_function(mapped_data):
    reduce_dict = {}    # Inicializa un diccionario vacío para almacenar los resultados reducidos.

    for key, value in mapped_data:  # Itera sobre cada tupla (clave, valor) en la lista de datos mapeados.
        if key in reduce_dict:  # Comprueba si la clave ya existe en el diccionario.
            reduce_dict[key] += value   # Si la clave existe, incrementa el valor existente en el diccionario con el valor de la tupla.
        else:
            reduce_dict[key] = value    # Si la clave no existe en el diccionario, la añade y establece su valor inicial al valor de la tupla.
        
    return reduce_dict  # Retorna el diccionario que contiene las claves y los valores acumulados.


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.append(map_function(line))  # Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
    
    reduced_data = reduce_function(mapped_data) # Aplicar la función reduce
    
    result = sorted(reduced_data.items())   # Convierte el diccionario `reduced_data` a una lista de tuplas y las ordena alfabéticamente por clave.
    return result   # Retorna la lista de tuplas ordenadas.


# Llamar a la función y obtener los resultados
resultado_mapreduce_suma = pregunta_03()
print(resultado_mapreduce_suma)

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide por tabulaciones.
    letters = parts[3].split(',')  # Extrae el cuarto elemento (index 3) de la línea.
    value = int(parts[1])  # Extrae el segundo elemento (index 1) de la línea como entero.
    return [(letter, value) for letter in letters]  # Retorna una tupla donde el primer elemento es el extraído anteriormente y el segundo elemento es el entero 'value'.


# Definición de la función `reduce_function` que acepta como argumento `mapped_data`, una lista de tuplas.
def reduce_function(mapped_data):
    reduce_dict = {}    # Inicializa un diccionario vacío para almacenar los resultados reducidos.

    for key, value in mapped_data:  # Itera sobre cada tupla (clave, valor) en la lista de datos mapeados.
        if key in reduce_dict:  # Comprueba si la clave ya existe en el diccionario.
            reduce_dict[key] += value   # Si la clave existe, incrementa el valor existente en el diccionario con el valor de la tupla.
        else:
            reduce_dict[key] = value    # Si la clave no existe en el diccionario, la añade y establece su valor inicial al valor de la tupla.
        
    return reduce_dict  # Retorna el diccionario que contiene las claves y los valores acumulados.


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.extend(map_function(line))  # OJO!!! Cambia append por extend aquí. Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
            # Se usa el método .extend() en lugar de .append() para añadir los elementos de la lista devuelta por map_function directamente a mapped_data sin anidarlos.
    
    reduced_data = reduce_function(mapped_data) # Aplicar la función reduce
    
    result = dict(sorted(reduced_data.items()))  # Crea un nuevo diccionario ordenando las claves alfabéticamente utilizando `sorted` sobre los elementos del diccionario.
    return result   # Retorna un diccionario de tuplas ordenadas.


# Llamar a la función y obtener los resultados
suma_letras = pregunta_11()
print(suma_letras)
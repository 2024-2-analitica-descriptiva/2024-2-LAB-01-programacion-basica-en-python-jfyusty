"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide en partes usando tabulaciones.
    key_values = parts[4].split(',')    # Extrae el quinta elemento (index 4) de la línea y la divide en segmentos por comas.
    result = [] # Inicializa una lista vacía para almacenar los resultados.
    for kv in key_values:   # Itera sobre cada segmento en la lista `key_values`.
        key, value = kv.split(':')  # Divide cada segmento por dos puntos para separar la clave del valor.
        result.append((key, int(value)))    # Añade una tupla a `result` donde el primer elemento es la clave y el segundo es el valor convertido a entero.
    return result   # Retorna la lista de tuplas resultante.


# Definición de la función `reduce_function` que acepta como argumento `mapped_data`, una lista de tuplas.
def reduce_function(mapped_data):
    reduce_dict = {}    # Inicializa un diccionario vacío para almacenar los resultados reducidos.

    for key, value in mapped_data:  # Itera sobre cada tupla (clave, valor) en la lista de datos mapeados.
        if key in reduce_dict:  # Comprueba si la clave ya existe en el diccionario.
            current_min, current_max = reduce_dict[key]     # Si la clave existe, extrae los valores actuales de mínimo y máximo asociados con la clave.
            reduce_dict[key] = (min(current_min, value), max(current_max, value))   # Actualiza el diccionario para esta clave estableciendo nuevos valores de mínimo y máximo.
            # Utiliza la función `min` para comparar el mínimo actual con el nuevo valor y seleccionar el menor.
            # Utiliza la función `max` para comparar el máximo actual con el nuevo valor y seleccionar el mayor.
        else:
            reduce_dict[key] = (value, value)    # Si la clave no existe en el diccionario, la añade y establece tanto el valor máximo como mínimo al valor actual.
            # Esto se hace porque es la primera vez que encontramos esta clave, por lo tanto, el primer valor es tanto el máximo como el mínimo.
    return reduce_dict  # Retorna el diccionario que contiene las claves y los valores acumulados.


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.extend(map_function(line))  # OJO!!! Cambia append por extend aquí. Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
            # Se usa el método .extend() en lugar de .append() para añadir los elementos de la lista devuelta por map_function directamente a mapped_data sin anidarlos.
    reduced_data = reduce_function(mapped_data) # Aplicar la función reduce
    
    result = [(k, v[0], v[1]) for k, v in sorted(reduced_data.items())]   # Convierte el diccionario `reduced_data` a una lista de tuplas y las ordena alfabéticamente por clave, luego el valor máximo y mínimo respectivamente.
    return result   # Retorna la lista de tuplas ordenadas.


# Llamar a la función y obtener los resultados
resultado_claves_min_max = pregunta_06()
print(resultado_claves_min_max)

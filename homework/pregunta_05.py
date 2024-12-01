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
            current_max, current_min = reduce_dict[key]     # Si la clave existe, extrae los valores actuales de máximo y mínimo asociados con la clave.
            reduce_dict[key] = (max(current_max, value), min(current_min, value))   # Actualiza el diccionario para esta clave estableciendo nuevos valores de máximo y mínimo.
            # Utiliza la función `max` para comparar el máximo actual con el nuevo valor y seleccionar el mayor.
            # Utiliza la función `min` para comparar el mínimo actual con el nuevo valor y seleccionar el menor.
        else:
            reduce_dict[key] = (value, value)    # Si la clave no existe en el diccionario, la añade y establece tanto el valor máximo como mínimo al valor actual.
            # Esto se hace porque es la primera vez que encontramos esta clave, por lo tanto, el primer valor es tanto el máximo como el mínimo.
    return reduce_dict  # Retorna el diccionario que contiene las claves y los valores acumulados.



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.append(map_function(line))  # Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
    
    reduced_data = reduce_function(mapped_data) # Aplicar la función reduce
    
    result = [(k, v[0], v[1]) for k, v in sorted(reduced_data.items())]   # Convierte el diccionario `reduced_data` a una lista de tuplas y las ordena alfabéticamente por clave, luego el valor máximo y mínimo respectivamente.
    return result   # Retorna la lista de tuplas ordenadas.


# Llamar a la función y obtener los resultados
resultado_max_min = pregunta_05()
print(resultado_max_min)

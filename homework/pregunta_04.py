"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide por tabulaciones.
    date = parts[2]   # Extrae el tercer elemento (index 2)
    month = date.split('-')[1]   # Extrae el segundo elemento de la lista "date" equivalente al mes (index 1).
    return (month, 1)   # Retorna una tupla donde el primer elemento es el extraído en "moth" y el segundo elemento es el entero 1.


# Definición de la función `reduce_function` que acepta como argumento `mapped_data`, una lista de tuplas.
def reduce_function(mapped_data):
    reduce_dict = {}    # Inicializa un diccionario vacío para almacenar los resultados reducidos.

    for key, value in mapped_data:  # Itera sobre cada tupla (clave, valor) en la lista de datos mapeados.
        if key in reduce_dict:  # Comprueba si la clave ya existe en el diccionario.
            reduce_dict[key] += value   # Si la clave existe, incrementa el valor existente en el diccionario con el valor de la tupla.
        else:
            reduce_dict[key] = value    # Si la clave no existe en el diccionario, la añade y establece su valor inicial al valor de la tupla.
        
    return reduce_dict  # Retorna el diccionario que contiene las claves y los valores acumulados.


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

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
resultado_meses = pregunta_04()
print(resultado_meses)

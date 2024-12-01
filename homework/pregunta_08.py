"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definición de la función `map_function` que toma como argumento una línea de texto.
def map_function(line):
    parts = line.strip().split('\t')    # Elimina los espacios en blanco al principio y al final de la línea y la divide en partes usando tabulaciones.
    number = parts[1]   # Extrae el segundo elemento (index 1) de la línea.
    letter = parts[0]   # Extrae el primer elemento (index 0) de la línea.
    return (number, letter) # Retorna la lista de tuplas resultante de 'number' y 'letter'..


# Definición de la función `reduce_function` que acepta como argumento `mapped_data`, una lista de tuplas.
def reduce_function(mapped_data):
    reduce_dict = {}    # Inicializa un diccionario vacío para almacenar los resultados reducidos.
    for number, letter in mapped_data:  # Itera sobre cada tupla (número, letra) en la lista de datos mapeados.
        if number in reduce_dict:    # Comprueba si el número ya existe en el diccionario.
            reduce_dict[number].add(letter)  # Si el número existe, añade la letra a la lista existente de letras asociadas con ese número.
            # Usar un conjunto evita duplicados y solo conserva valores únicos.
        else:
            reduce_dict[number] = {letter}  # Si el número no existe en el diccionario, crea una nueva entrada con el número como clave e inicializa el valor como un conjunto que contiene la letra.
            # Un conjunto se inicializa con `{letter}` para garantizar que futuras adiciones sean únicas.
    return reduce_dict  # Retorna el diccionario que contiene los números con sus respectivas listas de letras asociadas.


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    file_path = 'files/input/data.csv' # fijar la dirección

    mapped_data = []    # Inicializa una lista vacía para almacenar los datos.

    with open(file_path, 'r') as file:  # Abre el archivo en la ruta especificada en modo de lectura.
        for line in file:   # Itera sobre cada línea en el archivo.
            mapped_data.append(map_function(line))  # Aplica la función `map_function` a la línea y añade el resultado a la lista `mapped_data`.
    reduced_data = reduce_function(mapped_data) # Aplicar la función reduce.
    
    result = sorted([(int(k), sorted(list(v))) for k, v in reduced_data.items()], key=lambda x: x[0])   # Convierte el diccionario `reduced_data` a una lista de tuplas y las ordena numéricamente por clave, luego la lista de letras unicas ordenadas asociadas con la clave.
    return result   # Retorna la lista de tuplas ordenadas.


# Llamar a la función y obtener los resultados
resultado_letras_asociadas_unicas = pregunta_08()
print(resultado_letras_asociadas_unicas)

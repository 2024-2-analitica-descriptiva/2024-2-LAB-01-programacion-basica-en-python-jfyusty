"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


# Definir una función para sumar la segunda columna del archivo CSV
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    file_path = 'files/input/data.csv' # fijar la dirección 

    total_suma = 0  # Inicializa una variable para almacenar la suma total de la segunda columna.
    
    with open(file_path, 'r') as file:  # Abrir el archivo en la ruta dada en modo de lectura.
        for line in file:   # Iterar sobre cada línea en el archivo abierto.
            columns = line.strip().split('\t')  # Eliminar espacios en blanco al principio y al final de la línea y dividirla en columnas usando tabulación como delimitador.
            total_suma += int(columns[1])   # Convertir el valor de la segunda columna (index 1) a entero y añadirlo a `total_suma`.
    return total_suma   # Retornar el valor total acumulado en `total_suma`.

# Llamar a la función y obtener la suma de la segunda columna
suma_segunda_columna = pregunta_01()
print(suma_segunda_columna)

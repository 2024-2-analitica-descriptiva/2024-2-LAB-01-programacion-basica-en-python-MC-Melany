"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


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
    with open("files/input/data.csv", "r") as file:  # Abriendo el archivo
        Cmeses = {}  # Diccionario para almacenar el conteo por mes
        
        for linea in file:
            columns = linea.strip().split("\t")  # Dividir línea en columnas
        
            if columns:
                fecha = columns[2]  # Extraer la fecha de la columna 3
                mes = fecha.split("-")[1]  # Obtener el mes (MM) de la fecha
                
                    # Incrementar el contador del mes
                if mes in Cmeses:
                       Cmeses[mes] += 1
                else:
                        Cmeses[mes] = 1

          # Ordenar los resultados por mes y convertirlos a lista de tuplas
        mesesN = sorted(Cmeses.items())
    return mesesN 



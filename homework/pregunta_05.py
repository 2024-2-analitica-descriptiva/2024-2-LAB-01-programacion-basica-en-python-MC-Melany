"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """   
    with open("files/input/data.csv","r") as file: #abriendo el archivo
          valorM = {}
          for linea in file:

            columns = linea.strip().split("\t")
            if columns:
                letra= columns[0]
                valor = int(columns[1])
                # Incrementar el contador de la letra
                if letra in valorM:
                    valorM[letra].append(valor)
                else:
                    valorM[letra] = [valor]
                    
          ValorMi_max = [(letra, max(valorM[letra]), min(valorM[letra])) for letra in sorted(valorM.keys())
        ]
    
    return ValorMi_max
    
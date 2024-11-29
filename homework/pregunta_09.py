"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """   
    with open("files/input/data.csv", "r") as file:
      valoresclave = {}
      for linea in file:
            columns = linea.strip().split("\t")  # Dividir la línea en columnas
            if columns:
              letras = columns[4]
              valorC=  letras.split(",")

              for elemento in valorC:
                    clave, valor = elemento.split(":")  # Separar clave y valor
                    valor = int(valor)  # Convertir el valor a entero
 

                    if clave in valoresclave:
                        valoresclave[clave] += 1
                    else:
                        valoresclave[clave] = 1

      return valoresclave
    

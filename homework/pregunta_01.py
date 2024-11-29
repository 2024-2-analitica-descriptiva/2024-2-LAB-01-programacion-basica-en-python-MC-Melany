"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("files/input/data.csv","r") as file: #abriendo el archivo
        
        suma=0
        for line in file: # iterar
            columnas = line.strip().split("\t") 
            suma += int(columnas[1]) #convertimos a enteros 

    return suma # mostramos la suma

    

if __name__ == "__main__":
    print(pregunta_01())


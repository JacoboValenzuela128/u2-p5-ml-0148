import numpy as np
import pandas as pd
# Arath Valenzuela NC:0148 (28/10/26)
## Datos de matriz 4x3
datos_alumno =[
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]
# Poner nombre a las columnas 
# Se le almacena la tabla en la variable pd (DataFrame)
print("+---+ Datos a partir de una matriz de 4x3 +---+")
df=pd.DataFrame(datos_alumno,columns=['CI','Marcas','Paquete'])
print(df)
# Datos a partir de un diccionario
print("+---+ Datos a partir de un diccionario +---+")
alumno_diccionario = {
 'nombre':['Farfán','Arath','Alexandro','Jazmín','Caleb','Yahir'],
 'califa':[60,90,100,80,70,50],
 'edad':[16,15,16,14,17,15]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("--------------------------")
print("Hecho por Arath Valenzuela")
print("--------+NC:0148+---------")
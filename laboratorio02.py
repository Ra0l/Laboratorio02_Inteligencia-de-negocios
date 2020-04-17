import pandas as pd
import numpy as np

#Series item c
aleratorio=pd.Series([2,4,6,8,10,12,14,16,18,20]);

#'Numero alartorios: '
print(aleratorio)

#"5 primeros numeros: ",
print(aleratorio[:5])
#"5 ultimos numeros: ",
print(aleratorio[-5:])
#"2 primeros numeros ",
print( aleratorio[:2])
#"2 ultimos numeros",
print( aleratorio[-2:])

print("------------------")
#Comodin DataFrame arreglos

ventas={'Meses':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],'Monto':[34556,345,45,23,45,67]}
data3=pd.DataFrame(ventas)
print(data3)
cols=data3.columns.tolist()
columna_to_move = "Monto"
new_position = 0
cols.insert(new_position,cols.pop(cols.index(columna_to_move)))
data3 = data3[cols]
print(data3)

print("-----------------------")

#leer archivo csv

df = pd.read_csv("Ventas.csv");
ventas = pd.DataFrame(df)
print(ventas)

print("------------")
#Ejercico 4


#Ejercico 5 a

ventas={'Meses':['Enero','Febrero','Marzo'],'Ventas':[34556,3454,4545]}
data3=pd.DataFrame(ventas)
print(data3)

print("Estadistica")
print(data3.describe())

#Ejercio 5 c
print("Ejercicio 6 C")
datos6=pd.DataFrame(np.array([[1000,2000,3000],
                              [9000,8000,7000],
                              [3500,4560,460]]))
print(datos6)

print("Media")
print(datos6.mean())
print("Correlacion")
print(datos6.corr())
print("Valor minimo")
print(datos6.min())
print("Valor maximo")
print(datos6.max())
print("Mediana")
print(datos6.median())
print("Desviacion estandar")
print(datos6.std())

print("Primera Columna")
print(datos6[0])
print("Dos primeras columnas")
print(datos6[[0,1]])
print("Primera fila y ultima columna")
print(datos6.iloc[0][2])
print("Valores de la primera fila")
print(datos6.loc[0])
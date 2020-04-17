import pandas as pd
import numpy as np
#Ejercicio 1
data=pd.Series(['Enero','Febrero','Marzo','Abril','Mayo','Junio'],index=[1,2,3,4,5,6])
print(data)
#Ejercicio 2
data2=pd.Series({"Texto":"Valor","Mil":1000,"Dos mil":2000,"Tres mil":3000})
print(data2)


#Comodin DataFrame
ventas={'Meses':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],'Monto':[34556,345,45,23,45,67]}
data3=pd.DataFrame(ventas)
print(data3)
print(data3.describe())
print(data3.mean())





datos=pd.DataFrame(np.array([['Enero','Febrero','Marzo'],
                       [40000,35000,50000],
                       [56000,60000,24000],
                       [88000,77000,55000]]))
print(datos)
#Numero de filas y columnas (f,c)
print('Filas y columnas',datos.shape)
#numero de filas
print('Filas',len(datos.index))
#numero de columnas
print('Columnas',len(datos.count()))


#dos
datos2=pd.DataFrame(np.array([[4000,5000,34555],
                              [1224,2434,466],
                              [344546,465765,5758]]))

print(datos2)
#Estadistica
print(datos2.describe())
#media
print('Media',datos2.mean())
#Correlacion
print('Correlacion: ',datos2.corr())

#Obtener el numeor de datos
print('Numero de datos: ',datos2.count())

print('Valor maximo: ',datos2.max())
print('Valor minimo',datos2.min())

print('Mediana: ',datos2.median())

print('Desviacion estandar',datos2.std())

#Imprimeri la primera columna
print(datos2[0])

#Trabajar con dos columnas
print("Dos columnas: ",datos2[[0,1]])

#Imprimir y/o seleccionar primera fila y ultima columna
print("Primera fila y ultima columna: ",datos2.iloc[0][2])
#Seleccionar primera fila
print("Seleccionar primera fila: ",datos2.loc[0])

print("--------------------------------")

import xlrd
archivo=pd.read_excel('Ventas02.xlsx',sheet_name='Ventas',skiprows=1)
datos3=pd.DataFrame(archivo)
print(datos3)

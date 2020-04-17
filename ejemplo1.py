import pandas as pd
import numpy as np
import matplotlib as mp

df = pd.read_csv("medallero_Panamericanos_Lima2019.csv");
print(df)

def calc_suma():
    print("La suma de la columna Oro es : ",df['Oro'].sum())
    print("La suma de la columna Plata es : ",df.Plata.sum())
    print("La suma de la columna Bronce es : ",np.sum(df['Bronce']))
    print(np.sum(df.Oro))

def calc_nro_elementos():
    print("La cantidad de elementos de la columna Oro es : ",len(df['Oro']))
    print("La cantidad de elementos de la columna Plata es : ",len(df.Plata))
    print("La cantidad de elementos de la columna Bronce es : ",df['Bronce'].count())
    print(df.Oro.count())
    print(np.size(df['Oro']))
    print(np.size(df.Oro))

def calc_media(redondeo=2):
    media= df.Plata.mean()
    media=round(media, redondeo)
    return media

def calc_mediana():
    numero = np.size(df.Plata)
    pos_mediana=round(numero/2)
    print('Posicion mediana: ', pos_mediana)
    mediana =df.Plata[pos_mediana-1]
    return mediana

def calc_moda():
    moda = df.Oro.mode()
    return moda
def calc_percenti():
    p90 = df.Oro.quantile(0.9)
    return  p90

if __name__=='__main__':
    calc_suma()
    calc_nro_elementos()
    print("El percentil 90 de Oro es: ",calc_percenti())
    print("La media de Plata: ",calc_media(redondeo=2))

    print("La mediana de Plata es: ", calc_mediana())

    print ("La moda de Oro es : ", calc_moda())
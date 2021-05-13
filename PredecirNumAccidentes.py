# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:01:09 2020

@author: Daniel Andres
"""
### IMPORTAR LIBRERÍAS ###
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### IMPORTAR LOS DATOS ###
data = pd.read_csv('Crash_Analysis_System_CAS_data.csv')

### ANALIZAR LOS DATOS ###
#Conocer la forma de los datos
print("Tamaño original de la base de datos: ")
print(data.shape) 
#Conocer el formato de los datos
#print(data.dtypes)
datadt = data.dtypes #Como en consola no se muestran completos se pone así para verlo en el explorador de variables

#Conocer los datos nulos
#print(data.isnull().sum())
datain = data.isnull().sum() #Como en consola no se muestran completos se pone así para verlo en el explorador de variables

### PROCESAMIENTO DE LOS DATOS ###
#Eliminar las columnas que no son necesarias
data = data.drop(['X', 'Y', 'OBJECTID_1', 'OBJECTID'], axis=1)
data = data.drop(['crashDirec','crashRPDir','crashRPSH','crashRPNew',
                  'trafficCon','roadLane','cornerRoad'], axis=1)

#Reducir el conjunto de datos y trabajar con los accidentes desde 2010
data = data.loc[(data['crashYear'] > 2010), :]

### VISUALIZACIÓN DE LOS DATOS ###
# Visualizar de manera de texto el número de muertos y heridos
ano_inicio = data.crashYear.min()
ano_final = data.crashYear.max()

fatal = data['fatalCount'].sum()
mayor = data['seriousInj'].sum()
menor = data['minorInjur'].sum()

print("El total de muertes en accidentes de tránsito desde el {}".format(ano_inicio))
print("hasta el {} es de {}".format(ano_final,fatal))
print("Mientras el número total de heridos graves es de {}".format(mayor))
print("y el de heridos menores es de {}".format(menor))

#Visualizar los muertos, heridos graves y heridos menores por año
fig, ax = plt.subplots(1, 3, figsize = (18, 5));
sns.barplot(x="crashYear", y="fatalCount", data=data, ax=ax[0]);
sns.barplot(x="crashYear", y="seriousInj", data=data, ax=ax[1]);
sns.barplot(x="crashYear", y="minorInjur", data=data, ax=ax[2]);
[ax[i].set_xlabel('Crash Year') for i in range(3)]
plt.tight_layout()

#Visualizar la severidad de los accidentes ocurridos
sns.countplot(y="crashSever",data=data,order='NMSF')

#Convertimos los datos tipos objetos en numéricos
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

for i in data:
    if data[i].dtype == 'object':
        encoder.fit(data[i].astype(str))
        data[i] = encoder.transform(data[i])
data = pd.get_dummies(data)

### ANÁLISIS DE MACHINE LEARNING ###
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

#Definir las variables dependientes e independientes
y = data['fatalCount']
X = data.drop('fatalCount', axis=1)

#Separar los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20,
                                                    random_state=1)

#Definir el algoritmo 
algoritmo = RandomForestRegressor(n_estimators=50)

#Entrenar el algoritmo
algoritmo.fit(X_train, y_train)

#Realizar una predicción
y_test_pred = algoritmo.predict(X_test)

#Cálculo de la precisión del modelo
#Calculo R2
print("La precisión del modelo analizando el valor de R2_Score es: ")
print(r2_score(y_test,y_test_pred))
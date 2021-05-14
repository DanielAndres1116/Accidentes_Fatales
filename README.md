# Accidentes_Fatales
## Predicción de los accidentes fatales en Nueva Zelanda 

### Descripción del Dataset y cómo se obtuvo
Los datos utilizados fueron extraídos del Sistema de Análisis de Choques (CAS), quienes registran los accidentes de tráfico que la policía de Nueva Zelanda ha reportado a la Agencia de Transporte. Cabe decir que no todos los choques son reportados a la policía y el nivel de información aumenta con el nivel de gravedad del accidente. Los datos están actualmente disponibles a partir del 1 de enero del 2000 y se actualizan trimestralmente. 

Aqui el dataset:
https://www.dropbox.com/s/uzzc82fhwc0mybb/Crash_Analysis_System_CAS_data.csv?dl=0

##### NOTA: este dataset no se subió al repositorio ya que era un archivo pesado. Se puede descargar en el link anterior.

### Objetivos
Los accidentes de tráfico constituyen un problema importante en nuestra sociedad de todo el mundo. La organización Mundial de la Salud (OMS) estimó que 1,25 millones de muertes estaban relacionadas con lesiones por accidentes de tránsito en el año 2010. Por ende, se hizo un proceso completo de Machine Learning, desde la obtención de los datos, la realización del análisis exploratorio de datos y la formulación de un problema del mundo real en un modelo de Machine Learning.  

![image](https://user-images.githubusercontent.com/43154438/118164069-4a951180-b3e8-11eb-8a98-da553c9f03b8.png)

##### Este es uno de los gráficos de importancia:

![image](https://user-images.githubusercontent.com/43154438/118164084-4e289880-b3e8-11eb-9e0b-bf9ae643f9e0.png)

##### N – Accidentes Sin heridos
##### M – Accidentes Con heridas menores
##### S – Accidentes Con heridas mayores
##### F – Accidentes Con personas muertas


Dado a que la visualización de los gráficos no solamente se trata de graficar los datos, sino que también es presentar información importante a las personas, acá se da un ejemplo de esto y utilizando los datos se muestra la cantidad de accidentes con muertos, heridos graves y lesiones que ha habido en el periodo de tiempo en el que se está trabajando.

### Conclusiones y resultados obtenidos
Se utilizó un algoritmo de Bosques Aleatorios de Decisión para hacer la predicción de si un accidente resulta fatal o no y se obtuvo:

![image](https://user-images.githubusercontent.com/43154438/118164189-6ef0ee00-b3e8-11eb-9609-77056d08ec1f.png)

Este tipo de análisis y modelos resulta útil para la prevención de accidentes por medio de la determinación de las características que más influyen en estos. La idea es hacer un enfoque en eliminar las dispociciones que más accidentes causan. 


# importar las bibliotecas necesarias, (en el caso de que la librería no esté realizar comando: pip install pandas)
from turtle import title
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

# diagrama de Caja
# cargando el conjunto de datos
iris = pd.read_csv('Codigo/Datasets/iris.csv')

# explorando los datos para graficar
# para visualizar las columnas del dataset iris.csv
print('Encabezados dataset iris.csv: ')
print(iris.columns.tolist(), '\n')
print(iris['sepal.length'].describe(), '\n')

# se crea la variable data como una lista, en python se conoce como "list comprehension".
data = [go.Box(y=iris[iris['variety'] == flor]['sepal.length'],
               name=flor,
               boxpoints='all') # es otra representación de los datos, que se muestra a la izquierda de las cajas.
        for flor in iris['variety'].unique()] # para recorrer cada tipo de flor presente en la variable class,
# esta estructura es la que nos permite crear una gráfica por cada categoría en un solo paso.

# se define el diseño
layout = go.Layout(title='Gráficas de Caja: Longitud del sépalo',
                   xaxis=dict(title='Tipo de Flor'),
                   yaxis=dict(title='Longitud'))

# se crea la figura
fig = go.Figure(data=data, layout=layout)

# se crea la visualización
pyo.plot(fig, filename='box_plot.html')

# ----------------------------------------------------------------------------------------------------------------

# otro ejemplo: Diagrama de caja horizontal
# se generan datos aleatorios para graficar
x0 = np.random.randn(50)
x1 = np.random.randn(50) + 2 # para cambiar la media

# se crea la figura
fig = go.Figure()

# se utiliza el argumento x en lugar de y para la gráfica horizontal
fig.add_trace(go.Box(x=x0, marker_color = 'darkblue'))
fig.add_trace(go.Box(x=x1, marker_color = 'royalblue'))

# se edita el diseño, para este caso el título de la gráfica
fig.update_layout(
    title={'text': "Diagrama de caja horizontal"})

# se crea la visualización
fig.show()

# ----------------------------------------------------------------------------------------------------------------

# otro ejemplo de diagrama de Caja
# cargando el conjunto de datos
tips = pd.read_csv('Codigo/Datasets/tips.csv') 
 
# explorando los datos para graficar 
print('Dataset tips.csv: ')
print(tips.head())
print('Encabezados dataset tips.csv: ')
print(tips.columns.tolist(), '\n')

# diagrama de caja con solo puntos
fig = px.strip(tips, x='day', y='tip')

fig.update_layout(
    title={'text': "Diagrama de caja solo con puntos"})

fig.show()

# ----------------------------------------------------------------------------------------------------------------

# otro ejemplo de diagrama de Caja - Modificación del algoritmo para calcular cuartiles
# se generan datos aleatorios para graficar
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# se crea la figura
fig = go.Figure()

# argumentos para graficar
fig.add_trace(go.Box(y=data, quartilemethod="linear", name="Modo de cuartil lineal"))
fig.add_trace(go.Box(y=data, quartilemethod="inclusive", name="Modo cuartil inclusivo"))
fig.add_trace(go.Box(y=data, quartilemethod="exclusive", name="Modo de cuartil exclusivo"))

# se edita el diseño
fig.update_traces(boxpoints='all', jitter=0)
fig.update_layout(
    title={'text': 'Modificación del algoritmo para calcular cuartiles'})

# se crea la visualización
fig.show()

# Fin
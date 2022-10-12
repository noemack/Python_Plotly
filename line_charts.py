# importar las bibliotecas necesarias, (en el caso de que la librería no esté realizar comando: pip install plotly)
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px


# gráfico de línea 1 (simple)
# se generan datos aleatorios para graficar
x = np.arange(8)

# se crea la figura
fig = go.Figure(data=go.Scatter(x=x, y=x**2))

# se edita el diseño
fig.update_layout(title='Gráfico de línea sencillo',
                  xaxis_title='Eje x',
                  yaxis_title='Eje y')

# se crea la visualización
fig.show()

# --------------------------------------------------------------------------------------------------------------------

# gráficos de línea 2
# se generan datos aleatorios para graficar
np.random.seed(42)

# se crean los datos para las variables
x_values = np.linspace(0,1,101) # devuelve espacios numéricos de manera uniforme en el intervalo escrito
y_values = np.random.randn(100) # crea una matriz de forma específica y la llena con valores aleatorios

# para crear la primera gráfica de línea
trace0 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='línea+sombreado',
                    fill='tozeroy') # agrega sombreado

# para crear la segunda gárafica de línea
trace1 = go.Scatter(x=x_values,
                    y=y_values+5, # se suma 5 para que las gráficas no se superpongan
                    mode='lines+markers',
                    name='línea+puntos')

# para crear la tercera gárafica de línea
trace2 = go.Scatter(x=x_values,
                    y=y_values-5, # se resta 5 para que las gráficas no se superpongan
                    mode='markers',
                    name='puntos')

# se define data como una lista
data = [trace0, trace1, trace2]

# se define el diseño
layout =go.Layout(title='Gráficas de línea')

# se crea la figura
fig = go.Figure(data=data, layout=layout)

# dos formas posibles para variar el rango del eje Y
#fig.update_layout(yaxis=dict(range=[-8,8]))
#fig.update_yaxes(range=[-8, 8])

# se crea la visualización
pyo.plot(fig, filename='line_chart.html')

# --------------------------------------------------------------------------------------------------------------------

# gráfico de línea y dispersión 3 - conjunto de datos Gapminder
# cargando el conjunto de datos
gapminder = px.data.gapminder()
print(gapminder)

# Explorando los datos para graficar
# encabezados
print('Encabezados: ')
print (gapminder.columns, '\n')

# primera y última fila
print('Primera y última fila: ')
print(gapminder.iloc[0])
print(gapminder.iloc[-1], '\n')

# visualización de todos lo continentes
print ('Continentes: ')
print(gapminder.continent.value_counts(), '\n')

# filtrar datos del 2002
gapminder2002 = gapminder.query('year == 2002')

# graficar continentes por color
fig = px.scatter(gapminder2002, 
                 x='gdpPercap', y='lifeExp', 
                 color='continent',
                 title='Desarrollo mundial en 2002',
                 labels={'gdpPercap': 'PIB per cápita', 'lifeExp': 'Esperanza de vida', 'continent': 'Continentes'})

# se crea la visualización
fig.show()

# Fin

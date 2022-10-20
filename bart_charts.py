# importar las bibliotecas necesarias, (en el caso de que la librería no esté realizar comando: pip install pandas)
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

# gráfico de barras 1 (simple)
# cargando el conjunto de datos
gapminder = px.data.gapminder()
print(gapminder)

# explorando los datos para graficar
# encabezados
print('Encabezados: ')
print (gapminder.columns, '\n')

# visualización de todos lo países
print ('Países: ')
print(gapminder.country.value_counts(), '\n')

# gráfico
data_portugal = px.data.gapminder().query("country == 'Portugal'")
fig = px.bar(data_portugal, x='year', y='pop')

# se edita el diseño
fig.update_layout(title='Gráfico de barras sencillo',
                  xaxis_title='Año',
                  yaxis_title='Población')
fig.show()

# --------------------------------------------------------------------------------------------------------------------

# gráfico de barras 2
# para leer el dataset
df = pd.read_csv('Codigo/Datasets/2018WinterOlympics.csv')

# para imprimir las primeras 5 filas del dataset
print(df.head(), '\n')

# primer gráfico: categorías países y variable continua el total de medallas por país
data = [go.Bar(x=df['NOC'],
               y=df['Total'])]

# se define el diseño
layout = go.Layout(title='Total de Medallas por país')

# se crea la figura
fig = go.Figure(data=data, layout=layout)
fig.update_xaxes(title_text="Países") # título eje X
fig.update_yaxes(title_text="Cantidad") # título eje Y

# se crea la visualización
pyo.plot(fig, filename='bart_chart_rank.html')

# -----------------------------------------------------------------------------------------------------------------

# grafico de barras 3: barras apiladas para cada tipo de medallas por país, oro, plata y bronce por país
trace0 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Oro',
                marker={'color':'#FFD700'})

trace1 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Plata',
                marker={'color':'#9EA0A1'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronce',
                marker={'color':'#CD7F32'})

# se define data como una lista
data = [trace0, trace1, trace2]

# se define el diseño
layout = go.Layout(title='Medallas por país',
                   barmode='stack') # para las barras apiladas

# se crea la figura
fig = go.Figure(data=data, layout=layout)
fig.update_layout(legend_title_text = "Medallas") # título de leyenda
fig.update_xaxes(title_text="Países") # título eje X
fig.update_yaxes(title_text="Cantidad") # título eje Y

# se crea la visualización
pyo.plot(fig, filename='bart_chart_medallas.html')

# -----------------------------------------------------------------------------------------------------------------

# ejemplo de agregar texto a las barras
# cargando el conjunto de datos
df = px.data.medals_long()

# visualizando el df
print(df.head())

# gráfico
fig = px.bar(df, x="medal", y="count", color="nation", text_auto=True)

# diseño
fig.update_layout(title='Medallas',
                  xaxis_title='Tipo de medallas',
                  yaxis_title='Cantidad de medallas')
fig.show()

# Fin

# Más ejemplos: https://plotly.com/python/bar-charts/
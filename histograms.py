# importar las bibliotecas necesarias, (en el caso de que la librería no esté realizar comando: pip install pandas)
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

# histogrma 1 (simple)
# cargando el conjunto de datos
df = pd.read_csv('Codigo/Datasets/auto-mpg.csv')

# explorando los datos para graficar
# para imprimir las columnas del dataset y estadísticas básica de la columna 'mpg'
print('Encabezados dataset auto-mpg.csv: ')
print(df.columns, '\n')
print(df['mpg'].describe(), '\n')

# se crea el histograma
data = [go.Histogram(x=df['mpg'],
        nbinsx=40, # cantidad de intervalos
        histnorm='percent')] # tipo de normalización, porcentaje de datos de cada intervalo

# se define el diseño
layout = go.Layout(title='Histograma 1',
                   xaxis=dict(title='Millas por galón'),
                   yaxis=dict(title='Porcentaje'))

# se crea la figura
fig = go.Figure(data=data, layout=layout)

# se crea la visualización
pyo.plot(fig, filename='histogram_mpg.html')

# -----------------------------------------------------------------------------------------------------------------

# histograma 2: especificar una función de agregación
# se generan datos para graficar
x = ["Manzanas","Manzanas","Manzanas","Naranjas", "Bananas"]
y = ["5","10","3","10","5"]

# se crea la figura
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="contar"))
fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="suma"))

# se crea la visualización
fig.show()

# -----------------------------------------------------------------------------------------------------------------

# histograma 3: por orden de categoría: las barras de histograma también se pueden ordenar en función de la lógica
# de ordenación de los valores categóricos mediante el atributo de orden de categoría del eje x
# cargando el conjunto de datos
df = px.data.tips()
print('dataset data.tips: ')
print(df)

# Explorando los datos para graficar
# encabezados
print('Encabezados: ')
print (df.columns, '\n')

# primera y última fila
print('Primera y última fila: ')
print(df.iloc[0])
print(df.iloc[-1], '\n')

# se crea la figura
fig = px.histogram(df, 
                   x="day", 
                   color="smoker", 
                   labels={'day':'Días'},
                   title="Histograma 3 - Cantidad de fumadores y no fumadores por día").update_xaxes(categoryorder='total descending')

# se crea la visualización
fig.show()

# -----------------------------------------------------------------------------------------------------------------

# histograma 4:  diferentes valores de una columna
fig = px.histogram(df, x="total_bill", color="sex", title="Histograma 4 - Total factura por sexo")
fig.show()

# -----------------------------------------------------------------------------------------------------------------

# histograma 5: datos categóricos y numéricos agrupados en el eje x
fig = px.histogram(df, 
                   x="day", 
                   y="total_bill", 
                   title="Histograma 5 - Total facturado por día", 
                   labels={'total_bill':' Total factura', 'day':'Días'}, 
                   category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))

fig.show()

# Fin


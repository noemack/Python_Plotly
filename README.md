# Python_Plotly
La idea de este repositorio es mostrar diferentes tipos de gráficos básicos que podemos crear utilizando Python:
diagramas de líneas, diagramas de dispersión, gráficos de área, gráficos de barras, barras de error, diagramas de caja, histogramas, mapas de calor, subgráficos, gráficos de ejes múltiples, gráficos polares y gráficos de burbujas.

Si tienen interés pueden explorar la siguiente página para encontrar más contenido referente a gráficos con la librería Plotly

[Python-Plotly](https://plotly.com/python/)


## Herramientas

- Python
- Visual Studio Code

> Tener en cuenta que en algunas partes el código puede estar comentado, quitar para probar las diferentes operaciones y funciones



## Esquema

> "line_charts", [Link](https://github.com/noemack/Python_Plotly/blob/main/line_charts.py)

##### Gráficos de líneas - Se utilizan para mostrar el valor cuantitativo en un intervalo o intervalo de tiempo continuo. Se usa con mayor frecuencia para mostrar tendencias y patrones de datos a lo largo del tiempo. Este tipo de gráfico es bastante útil cuando se muestran líneas de tendencia con diferencias sutiles, o con líneas de datos que se cruzan entre sí.

`Librerías utilizadas: `
```
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

```
---

> "bart_charts", [Link](https://github.com/noemack/Python_Plotly/blob/main/bart_charts.py)

##### Gráficos de barras - Son útiles para resumir variables categóricas y comparar dos o más valores. Resumen y comparan los datos categóricos mediante longitudes de barras proporcionales para representar valores.

`Librerías utilizadas: `
```
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

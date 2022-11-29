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

##### Gráficos de líneas 
> Se utilizan para mostrar el valor cuantitativo en un intervalo o intervalo de tiempo continuo. Se usa con mayor frecuencia para mostrar tendencias y patrones de datos a lo largo del tiempo. Este tipo de gráfico es bastante útil cuando se muestran líneas de tendencia con diferencias sutiles, o con líneas de datos que se cruzan entre sí.

`Librerías utilizadas: `
```
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

```
---

> "bart_charts", [Link](https://github.com/noemack/Python_Plotly/blob/main/bart_charts.py)

##### Gráficos de barras
> Son útiles para resumir variables categóricas y comparar dos o más valores. Resumen y comparan los datos categóricos mediante longitudes de barras proporcionales para representar valores.

`Librerías utilizadas: `
```
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

---

> "histograms", [Link](https://github.com/noemack/Python_Plotly/blob/main/histograms.py)

##### Histogramas
> Son útiles representar la distribución de datos numéricos, donde los datos se agrupan y se representa el recuento de cada contenedor. Un histograma es un gráfico de barras agregado, con varias funciones de agregación posibles (suma, promedio, conteo...) que se pueden usar para visualizar datos en ejes categóricos y de fecha, así como ejes lineales.

`Librerías utilizadas: `
```
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

---

> "box_plots", [Link](https://github.com/noemack/Python_Plotly/blob/main/box_plots.py)

##### Diagramas de Caja
> El diagrmaa de caja es una representación estadística de la distribución de una variable a través de sus cuartiles. Los extremos de la caja representan los cuartiles inferior y superior, mientras que la mediana (segundo cuartil) está marcada por una línea dentro de la caja.
Son útiles para mostrar o comparar una distribución de datos, identificar el mínimo, el máximo y la mediana de los datos. Proporciona un resumen visual de los datos, permitiendo a los investigadores identificar rápida y fácilmente los valores medios, así como la dispersión del conjunto de datos, incluidos los signos de asimetría.

`Librerías utilizadas: `
```
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

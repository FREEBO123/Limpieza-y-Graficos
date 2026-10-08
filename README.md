Proyecto de limpieza de datos y generacion de graficos

Descripción del Proyecto:

haciendo uso del archivo exportado en el modulo anterior, hare una serie de transformaciones para hacer mas digerible la informacion y generare una serie de graficos para transformar la data en informacion visual que facilite su entendimiento, este es un paso crucial en el analisis de datos.

1. Leer y transformar la informacion

    Se uso Pandas para leer y manipular la data, se quitaron indices y columnas sin aporte estadistico,
    mediante el uso de la funcion melt, se reordeno la info para simplificar las transformaciones posteriores, ya que de esta forma se reduce el numero de columnas

2. Exportar Dataframe resultante

    Cree un archivo excel con la informacion ya transformada, esto con el fin de ejemplificar como queda la informacion despues de las transformaciones

3. Graficando la informacion

    Mediante el uso de la libreria Matplotlib, se crearon una serie de graficos y fueron exportados a formato png
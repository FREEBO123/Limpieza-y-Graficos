import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Ruta archivo a trabajar
ruta = "C:/Users/dell/Downloads/PROYECTO PORTAFOLIO/Modulos/Web Scraping/datos.xlsx"
hoja = "Sheet1"

# Lector de archivo (omitiendo primera fila que corresponde a un indice)
df = pd.read_excel(ruta,sheet_name=hoja,skiprows=1)

# Quitando la Primera columna que corresponde a un formulario sin valor estadistico
df = df.iloc[:, 1:]
df.reset_index(drop=True, inplace=True)

# Reordenando la informacion para facilitar su manipulacion
df = df.melt("Serie",value_name="Tasa_Crecimiento",var_name="Periodo")

# Asignando formatos numericos
df["Tasa_Crecimiento"] = df["Tasa_Crecimiento"].astype(str).str.replace(",",".", regex=False)
df["Tasa_Crecimiento"] = pd.to_numeric(df["Tasa_Crecimiento"],errors="coerce")

# Separando el trimestre del año
df[["Trimestre", "Año"]] = df["Periodo"].str.split(".", expand=True)
df["Año"] = pd.to_numeric(df["Año"],errors="coerce")

df["Trimestre"] = df["Trimestre"].replace({
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4
})

# extraere la informacion en un archivo excel para ejemplificar su estado despues de las transformaciones
df.to_excel("Datos transformados.xlsx",index=False)

# Supongamos que me interesa saber el desempeño de chile los ultimos 3 años
df = df[df["Año"]>=2023]
df_chile = df[df["Serie"]=="Chile"].sort_values(by=["Año","Trimestre"],ascending=[True,True])

plt.plot(df_chile["Periodo"],df_chile["Tasa_Crecimiento"])
plt.xticks(rotation=45, ha="right")
plt.title("Tasa Crecimiento Chile 2023-2026")
plt.tight_layout()
plt.savefig("Crecimiento Chile")

# A hora supongamos que quiero comparar el desempeño de chile con otros paises de la region, 
# en este caso peru y argentina
df_peru = df[df["Serie"]=="Perú"].sort_values(by=["Año","Trimestre"],ascending=[True,True])
df_argentina= df[df["Serie"]=="Argentina"].sort_values(by=["Año","Trimestre"],ascending=[True,True])

plt.plot(
    df_chile["Periodo"],
    df_chile["Tasa_Crecimiento"],
    label="Chile"
)

plt.plot(
    df_peru["Periodo"],
    df_peru["Tasa_Crecimiento"],
    label="Perú"
)

plt.plot(
    df_argentina["Periodo"],
    df_argentina["Tasa_Crecimiento"],
    label="Argentina"
)

plt.xticks(rotation=45, ha="right")
plt.legend()
plt.title("Tasa Crecimiento Region Sur 2023-2026")
plt.tight_layout()
plt.savefig("Region Sur")
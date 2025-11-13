import pandas as pd
import matplotlib.pyplot as plt

# ---------- 1. Leer y preparar ----------
df = pd.read_csv("Border_Crossing_Entry_Data.csv")

# Normalizar nombres de columna: todo en minúsculas y sin espacios
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Mostrar columnas para verificar
print("Columnas:", df.columns.tolist())

# Asegurarnos de que la columna de fecha se convierta bien (pandas infiere)
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Comprobar si la columna del puerto existe (puede llamarse post_name o port_name)
if "post_name" in df.columns:
    port_col = "post_name"
elif "port_name" in df.columns:
    port_col = "port_name"
else:
    raise KeyError("No se encontró columna 'Post Name' ni 'Port Name' en el CSV. Columnas disponibles: "
                   + ", ".join(df.columns))

print("Usando columna de puerto:", port_col)

# ---------- 2. Serie total por mes ----------
serie_total = df.groupby("date")["value"].sum().sort_index()

plt.figure(figsize=(12,5))
plt.plot(serie_total.index, serie_total.values, marker="o")
plt.title("Total de cruces por mes")
plt.xlabel("Mes")
plt.ylabel("Total de cruces")
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()

# ---------- 3. Cruces por tipo de transporte ----------
if "measure" in df.columns:
    serie_transport = df.groupby(["date", "measure"])["value"].sum().unstack(fill_value=0)
    plt.figure(figsize=(12,5))
    serie_transport.plot(marker="o", figsize=(12,5))
    plt.title("Cruces por tipo de transporte por mes")
    plt.xlabel("Mes")
    plt.ylabel("Número de cruces")
    plt.grid(True)
    plt.legend(title="Measure")
    plt.gcf().autofmt_xdate()
    plt.show()
else:
    print("No se encontró columna 'measure' — se omitió gráfico por tipo de transporte.")

# ---------- 4. Cruces por punto fronterizo (top 5) ----------
# Creamos la tabla serie_port (filas: date, columnas: puerto)
serie_port = df.groupby(["date", port_col])["value"].sum().unstack(fill_value=0)

# Calculamos los 5 puertos con mayor total de cruces en todo el periodo
top_ports = df.groupby(port_col)["value"].sum().nlargest(5).index.tolist()
print("Top 5 puertos:", top_ports)

# Filtramos serie_port por esos puertos y graficamos
serie_top = serie_port[top_ports]

plt.figure(figsize=(12,6))
serie_top.plot(marker="o", figsize=(12,6))
plt.title("Cruces mensuales — Top 5 puntos fronterizos")
plt.xlabel("Mes")
plt.ylabel("Número de cruces")
plt.legend(title="Punto fronterizo")
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()

# 📊 Análisis de Cruces Fronterizos – Border Crossing Entry Data

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) 
[![GitHub stars](https://img.shields.io/github/stars/Powfip/book_analysis?style=social)](https://github.com/Powfip/book_analysis/stargazers) 
[![Made with VSCode](https://img.shields.io/badge/Made%20with-VSCode-blue?logo=visual-studio-code)](https://code.visualstudio.com/)

Este proyecto realiza un **análisis de cruces fronterizos** utilizando el dataset `Border_Crossing_Entry_Data.csv`.  
Se generan gráficos de:

- Total de cruces por mes  
- Cruces por tipo de transporte (si existe la columna `measure`)  
- Top 5 puntos fronterizos con más cruces  

---

## 🗂 Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `border_analysis.py` | Script principal que procesa los datos y genera los gráficos. |
| `Border_Crossing_Entry_Data.csv` | Dataset con información de cruces fronterizos. |

---

## ⚡ Requisitos

Python 3.10+ y las siguientes librerías:

```bash
pip install pandas matplotlib
```

---

## 🏃‍♂️ Cómo usar el proyecto

1️⃣ **Ejecutar el análisis**

```bash
python border_analysis.py
```

2️⃣ El script realiza automáticamente:

- Limpieza de datos: convierte nombres de columnas a minúsculas y reemplaza espacios por `_`.  
- Conversión de fechas a formato `datetime`.  
- Selección de la columna correcta de puerto (`post_name` o `port_name`).  

3️⃣ Genera gráficos:

- **Total de cruces por mes**

```python
plt.plot(serie_total.index, serie_total.values, marker="o")
```

- **Cruces por tipo de transporte** (si existe `measure`)

```python
serie_transport.plot(marker="o", figsize=(12,5))
```

- **Top 5 puertos fronterizos**

```python
serie_top.plot(marker="o", figsize=(12,6))
```

---

## 📊 Visualizaciones esperadas

1. **Total de cruces por mes**  
   ![total_mes](examples/total_mes.png)

2. **Cruces por tipo de transporte**  
   ![transport](examples/transport.png)

3. **Top 5 puntos fronterizos**  
   ![top_ports](examples/top_ports.png)

> *Tip:* Guarda tus gráficos en la carpeta `examples` para mostrarlos en GitHub.

---

## 💡 Notas importantes

- El script detecta automáticamente la columna de puerto disponible (`post_name` o `port_name`).  
- Si la columna `measure` no existe, se omite el gráfico por tipo de transporte.  
- Se recomienda revisar los datos y asegurar que `date` y `value` estén presentes en el CSV.

---

## 🚀 Posibles mejoras

- Agregar análisis por tipo de vehículo o trenes específicos.  
- Filtrar por año o por punto fronterizo.  
- Crear dashboards interactivos con `plotly` o `streamlit`.  
- Guardar automáticamente los gráficos como imágenes (`.png`).  

---

## 🔗 Referencias

- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  

---

## 📧 Contacto

Si tienes dudas o sugerencias, puedes escribirme a:  
**123filipi@gmail.com**

---

## 🌟 Contribuciones

Si quieres mejorar este proyecto, eres bienvenido a hacer **fork** y **pull request**.  

---

🎉 ¡Analiza cruces fronterizos, visualiza tendencias y practica análisis de datos con Python! 🚀

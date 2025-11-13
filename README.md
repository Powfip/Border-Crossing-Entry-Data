# 📊 Border Crossing Entry Data – Análisis de Datos

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) 
[![GitHub stars](https://img.shields.io/github/stars/Powfip/border-crossing-analysis?style=social)](https://github.com/Powfip/border-crossing-analysis/stargazers) 
[![Made with VSCode](https://img.shields.io/badge/Made%20with-VSCode-blue?logo=visual-studio-code)](https://code.visualstudio.com/)

**Border Crossing Entry Data – Análisis de Datos** es un proyecto en Python para **analizar cruces fronterizos en EE.UU.**, estudiar la evolución mensual total, por tipo de transporte y por puerto, y generar gráficos de series temporales.

---

## 🗂 Archivos del proyecto

| Archivo                          | Descripción |
|---------------------------------|-------------|
| `analysis.py`                    | Script que analiza los datos y genera gráficos de cruces por mes, por tipo de transporte y top 5 puertos. |
| `Border_Crossing_Entry_Data.csv` | Dataset oficial (opcional, solo para análisis; se puede descargar del sitio del gobierno). |

---

## ⚡ Requisitos

Python 3.10+ y las siguientes librerías:

```bash
pip install pandas matplotlib
🏃‍♂️ Cómo usar el proyecto
1️⃣ Ejecutar el análisis
python analysis.py
Carga y limpia el dataset: normaliza nombres de columna, convierte la columna Date a datetime y detecta automáticamente la columna de puerto (Post Name o Port Name).
Calcula series temporales:
Total de cruces por mes
Cruces por tipo de transporte
Cruces por los 5 puertos con mayor total de cruces
Genera gráficos automáticamente:
📊 Serie temporal total de cruces
📈 Cruces por tipo de transporte
🔹 Top 5 puertos fronterizos
📊 Ejemplos visuales
Total cruces por mes	Cruces por tipo de transporte	Top 5 puertos fronterizos
Consejo: Guarda tus gráficos generados en la carpeta examples para mostrarlos en GitHub.
💡 Notas importantes
No es necesario subir Border_Crossing_Entry_Data.csv; otros pueden generar sus propios análisis descargando el dataset oficial.
Los gráficos se generan con matplotlib y se pueden personalizar fácilmente.
Se muestra automáticamente la top 5 de puertos con mayor número de cruces totales.
🚀 Posibles mejoras
Analizar tendencias estacionales por tipo de medida.
Crear dashboards interactivos con plotly o streamlit.
Guardar automáticamente los gráficos como imágenes (.png).
Filtrar datos por frontera o por puerto específico.
🔗 Referencias
BTS Border Crossing Data
Pandas Documentation
Matplotlib Documentation
📧 Contacto
Si tienes dudas o sugerencias sobre el proyecto, puedes escribirme a:
123filipi@gmail.com
🌟 Contribuciones
Si quieres mejorar este proyecto, eres bienvenido a hacer fork y pull request. Toda contribución será bien recibida.
🎉 ¡Analiza cruces fronterizos, estudia tendencias y practica análisis de datos en Python! 🚀

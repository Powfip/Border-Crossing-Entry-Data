# 📚 Book Scraper & Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) 
[![GitHub stars](https://img.shields.io/github/stars/Powfip/book_analysis?style=social)](https://github.com/Powfip/book_analysis/stargazers) 
[![Made with VSCode](https://img.shields.io/badge/Made%20with-VSCode-blue?logo=visual-studio-code)](https://code.visualstudio.com/)

**Book Scraper & Analysis** es un proyecto en Python para **extraer información de libros** de [Books to Scrape](https://books.toscrape.com/), analizar precios, ratings y disponibilidad, y generar gráficos con estadísticas básicas.  

---

## 🗂 Archivos del proyecto

| Archivo             | Descripción |
|--------------------|-------------|
| `scraper_book.py`   | Script que obtiene los datos de los libros y los guarda en `libros.csv`. |
| `analysis.py`       | Script que analiza los datos y genera gráficos de precios y ratings. |
| `libros.csv`        | CSV generado por `scraper_book.py` (opcional, solo para análisis). |

---

## ⚡ Requisitos

Python 3.10+ y las siguientes librerías:

```bash
pip install pandas matplotlib beautifulsoup4 requests
```

---

## 🏃‍♂️ Cómo usar el proyecto

### 1️⃣ Ejecutar el scraper

```bash
python scraper_book.py
```

- Descarga **1000 libros** (50 páginas).  
- Crea `libros.csv` con las columnas:
  - `titulo` → Título del libro  
  - `precio` → Precio en libras (£)  
  - `rating` → Valoración (`One` a `Five`)  
  - `disponibilidad` → Stock disponible  

---

### 2️⃣ Ejecutar el análisis

```bash
python analysis.py
```

- Convierte y limpia los datos:
  - Precio a número flotante  
  - Rating de texto a número  
- Muestra estadísticas:
  - Número total de libros  
  - Precio medio, mínimo y máximo  
  - Conteo de libros por rating  
- Genera gráficos automáticamente:
  1. 📊 Histograma de precios  
  2. 📈 Precio medio por rating (barras)  
  3. 🔹 Scatter plot: precio vs rating  

---

## 📊 Ejemplos visuales

| Histograma de precios | Precio medio por rating | Scatter precio vs rating |
|----------------------|-----------------------|------------------------|
| ![histograma](examples/histograma.png) | ![barras](examples/barras.png) | ![scatter](examples/scatter.png) |

> *Consejo:* Guarda tus gráficos generados en la carpeta `examples` para mostrarlos en GitHub.

---

## 💡 Notas importantes

- No es necesario subir `libros.csv`; otros pueden generar sus propios datos ejecutando `scraper_book.py`.  
- Asegúrate de usar la codificación correcta al leer CSV (`utf-8` o `latin-1`).  
- Los gráficos se generan con `matplotlib` y se pueden personalizar fácilmente.  

---

## 🚀 Posibles mejoras

- Filtrar libros por disponibilidad (`in stock`).  
- Analizar más a fondo la relación entre precio y rating.  
- Crear dashboards interactivos con `plotly` o `streamlit`.  
- Guardar automáticamente gráficos como imágenes (`.png`).  

---

## 🔗 Referencias

- [Books to Scrape](https://books.toscrape.com/)  
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)  

---

## 📧 Contacto

Si tienes dudas o sugerencias sobre el proyecto, puedes escribirme a:  
**123filipi@gmail.com**

---

## 🌟 Contribuciones

Si quieres mejorar este proyecto, eres bienvenido a hacer **fork** y **pull request**. Toda contribución será bien recibida.

---

🎉 ¡Explora libros, analiza precios y ratings, y practica análisis de datos en Python! 🚀

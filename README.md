# clasificacion-de-vinos

# 🍷 Clasificación de Vinos

Proyecto de análisis exploratorio de datos (EDA) y clasificación de la calidad de vinos utilizando modelos de machine learning en Python.

---

## 📌 Objetivo

El objetivo de este proyecto es analizar un conjunto de datos de vinos y construir modelos de clasificación que permitan predecir la calidad del vino a partir de sus características fisicoquímicas.

---

## 📂 Estructura del proyecto

```
clasificacion-de-vinos/
│
├── src/
│   ├── eda.py
│   ├── entrenamiento.py
│   ├── prueba.py
│   ├── modelo.pkl
│
├── WineQT.csv
└── README.md
```

---

## 🔍 Análisis Exploratorio de Datos (EDA)

En el módulo `eda.py` se realiza:

* Carga del dataset
* Análisis de valores nulos
* Estadísticas descriptivas
* Visualización de distribuciones
* Detección de outliers mediante boxplots
* Matriz de correlación

---

## 🤖 Modelos de Machine Learning

En el módulo `entrenamiento.py` se implementan dos modelos:

* 🌲 Random Forest
* 📈 Regresión Logística

Se evalúan utilizando:

* Accuracy
* Precision
* Recall
* F1-score

El mejor modelo es guardado como:

```
modelo.pkl
```

---

## 📊 Evaluación del modelo

En `prueba.py` se realiza:

* Carga del modelo entrenado
* Predicción sobre los datos
* Matriz de confusión
* Reporte de clasificación

---

## 📈 Resultados

El modelo obtuvo aproximadamente:

* **Accuracy:** 93%
* Buen desempeño en la mayoría de las clases
* Mejor rendimiento en clases con mayor número de muestras


## 🚀 Tecnologías utilizadas

* Python
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* joblib

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

```
git clone https://github.com/tu-usuario/clasificacion-de-vinos.git
```

2. Entrar a la carpeta:

```
cd clasificacion-de-vinos/src
```

3. Ejecutar los scripts:

```
python eda.py
python entrenamiento.py
python prueba.py
```

---

## 📌 Autor

Proyecto académico para la materia de Arquitectura de Sistemas de IA.

---

# Predicción del Ganador de la Copa Mundial de Fútbol 2026

## 📋 Descripción del Proyecto

Este proyecto utiliza técnicas de ciencia de datos y machine learning para predecir el ganador de la Copa Mundial de Fútbol FIFA 2026. Se analizan datos históricos de ediciones anteriores del torneo, considerando estadísticas de desempeño, rendimiento en grupos y patrones históricos.

## 🎯 Objetivo Principal

Desarrollar un modelo predictivo que sea capaz de:

- **Predecir el ganador** de la Copa Mundial 2026
- **Estimar puntos esperados** por equipo en la fase de grupos
- **Evaluar probabilidades** de clasificación y progresión en el torneo

## 🔍 Función de Predicción de Puntos

La función de predicción de puntos es el corazón del modelo. Esta función:

1. **Analiza datos históricos**: Revisa el desempeño de cada equipo en mundiales anteriores
2. **Calcula probabilidades de resultado**: Determina la probabilidad de victoria, empate o derrota según:
   - Rankings FIFA históricos
   - Desempeño previo en grupos
   - Rendimiento contra equipos de similar nivel
3. **Asigna puntos esperados**:
   - Victoria = 3 puntos
   - Empate = 1 punto
   - Derrota = 0 puntos
4. **Proyecta totales**: Suma los puntos esperados para toda la fase de grupos

Esta predicción permite estimar cuáles equipos es más probable que clasifiquen a fases posteriores.

## 📁 Estructura del Proyecto

```
│
├── README.md                           # Este archivo
├── recoleccion_datos.py               # Script para recolectar y descargar datos
├── limpieza_datos.ipynb               # Notebook: limpieza y preparación de datos
├── grupos.ipynb                       # Notebook: análisis de grupos y clasificaciones
├── modelo.ipynb                       # Notebook: construcción y evaluación del modelo
│
└── datos/                             # Carpeta con datos del proyecto
    ├── Mundiales_FIFA_fixture.csv                      # Datos crudos de fixtures
    ├── Mundiales_FIFA_registro_historico.csv           # Registro histórico de partidos
    ├── D_Mundiales_FIFA_fixture_limpio.csv             # Fixtures procesado
    └── Clean_Mundiales_FIFA_registro_historico_limpio.csv # Histórico procesado
```

## 🛠️ Componentes Principales

### 1. **Recolección de Datos** (`recoleccion_datos.py`)

- Obtiene datos históricos de mundiales anteriores
- Descarga información de fixtures y resultados
- Prepara los datos en formato CSV

### 2. **Limpieza de Datos** (`limpieza_datos.ipynb`)

- Eliminación de valores faltantes
- Estandarización de nombres de países
- Tratamiento de outliers
- Validación de integridad de datos

### 3. **Análisis de Grupos** (`grupos.ipynb`)

- Análisis de desempeño histórico por país
- Estadísticas en fases de grupos
- Identificación de patrones y tendencias

### 4. **Construcción del Modelo** (`modelo.ipynb`)

- Entrenamiento del modelo predictivo
- Validación y evaluación del desempeño
- Predicción para la Copa Mundial 2026

## 📊 Datos Utilizados

El proyecto utiliza datos históricos de Copas Mundiales incluyendo:

- **Resultados de partidos**: Goles, equipos, fases
- **Información de grupos**: Clasificaciones, puntos, diferencia de goles
- **Calendarios**: Fixture de grupos y enfrentamientos

## 🚀 Instrucciones de Uso

### Requisitos Previos

```bash
python >= 3.8
jupyter notebook
pandas
numpy
scikit-learn
matplotlib
seaborn
```

### Pasos para Ejecutar

1. **Recolectar datos** (si es necesario):

   ```bash
   python recoleccion_datos.py
   ```

2. **Abrir los notebooks** en orden:
   - Primero: `limpieza_datos.ipynb`
   - Luego: `grupos.ipynb`
   - Finalmente: `modelo.ipynb`

3. **Ejecutar las celdas** en cada notebook para:
   - Procesar y limpiar datos
   - Generar visualizaciones
   - Entrenar el modelo
   - Obtener predicciones

## 📈 Resultados Esperados

El modelo proporciona:

- ✅ Predicción del ganador del mundial 2026
- ✅ Top 10 equipos más probables de ganar
- ✅ Puntos esperados por equipo en grupos
- ✅ Probabilidades de clasificación
- ✅ Visualizaciones de predicciones y análisis

## 🔬 Metodología

- **Técnicas aplicadas**: Análisis estadístico, machine learning, predicción probabilística
- **Validación**: Validación cruzada y evaluación en datos históricos
- **Confiabilidad**: El modelo se valida contra resultados reales de mundiales anteriores

## ⚠️ Limitaciones y Consideraciones

- El modelo se basa en datos históricos; eventos inesperados (lesiones, cambios políticos) no se consideran
- Las predicciones mejoran con datos más recientes y actualizados
- Los resultados son estimaciones probabilísticas, no certezas

## 📝 Autor

Proyecto de Ciencia de Datos - Análisis de Mundiales FIFA

---

**Nota**: Este proyecto es un ejercicio educativo de ciencia de datos y predicción estadística.

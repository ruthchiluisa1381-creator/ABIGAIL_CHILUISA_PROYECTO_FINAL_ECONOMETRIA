# Proyecto Final de Econometría Aplicada: Análisis ENEMDU (2024-2025)

## [Desplegado en Vercel] https://abigail-chiluisa-proyecto-final-eco-sable.vercel.app
## [Código en GitHub] https://github.com/ruthchiluisa1381-creator/ABIGAIL_CHILUISA_PROYECTO_FINAL_ECONOMETRIA.git

## 📌 Datos Generales
* **Autor:** Abigail Chiluisa
* **Institución:** Universidad Técnica de Cotopaxi
* **Materia:** Econometría Aplicada
* **Modalidad Econométrica:** Modalidad A — Modelos de Respuesta Binaria (Logit y Probit)

---

## 🎯 Problema de Investigación y Objetivos

### Problema de Investigación
Analizar los determinantes socioeconómicos y demográficos que condicionan la probabilidad de inserción en el mercado laboral / informalidad en el Ecuador utilizando microdatos oficiales de la ENEMDU.

### Pregunta de Investigación
¿Cuáles son los factores socioeconómicos que influyen significativamente en la probabilidad de empleo o informalidad laboral en la Población en Edad de Trabajar (PET) en Ecuador durante el periodo 2024-2025?

### Objetivos
1. **Objetivo General:** Estimar y comparar modelos econométricos de respuesta binaria (Logit y Probit) para evaluar la probabilidad de inserción laboral en Ecuador.
2. **Objetivos Específicos:**
   * Procesar y limpiar la base de datos de la ENEMDU aplicando los factores de expansión correspondientes.
   * Evaluar la capacidad predictiva y ajuste econométrico mediante matriz de confusión, curva ROC, AUC y criterios de información (AIC/BIC).
   * Calcular e interpretar los Efectos Marginales Promedio (AME) para discutir implicaciones económicas y de política pública.

---

## 📊 Fuente de Datos y Variables

* **Fuente de Información:** Instituto Nacional de Estadística y Censos (INEC) — Encuesta Nacional de Empleo, Desempleo y Subempleo (**ENEMDU 2024-2025**).
* **Unidad de Observación:** Personas en Edad de Trabajar (PET) en el Ecuador.
* **Diccionario de Variables:** Disponible en detalle en [`data/diccionario_variables.md`](./data/diccionario_variables.md).

---

## 📁 Estructura Real del Repositorio

```text
ABIGAIL_CHILUISA_PROYECTO_FINAL_ECONOMETRIA/
├── README.md                          # Documentación principal del proyecto
├── requirements.txt                   # Librerías necesarias de Python
├── .gitignore                         # Archivos ignorados por Git
├── LICENSE                            # Licencia del proyecto
├── dashboard/                         # Aplicación web para Vercel
│   ├── outputs/
│   │   ├── figures/                   # Gráficos generados
│   │   │   ├── curva_roc.png
│   │   │   ├── distribucion_edad_inf...
│   │   │   └── efectos_marginales.png
│   │   ├── results/                   # Resultados en formato de texto y JSON
│   │   │   ├── metricas_json.json
│   │   │   └── resumen_modelos.txt
│   │   └── tables/                    # Tablas estadísticas y econométricas
│   │       ├── matriz_confusion.csv
│   │       ├── matriz_confusion.json
│   │       ├── resultados_logit_probi...
│   │       ├── tabla_descriptiva.csv
│   │       └── tabla_descriptiva.tex
│   ├── public/                        # Archivos estáticos
│   ├── src/app/                       # Componentes de la interfaz
│   │   └── page.jsx
│   └── package.json                   # Configuración del proyecto web
├── data/
│   ├── processed/                     # Base de datos procesada
│   │   └── enemdu_procesado.csv
│   ├── raw/                           # Datos originales descargados del INEC
│   └── diccionario_variables.md       # Diccionario descriptivo de variables
├── notebooks/                         # Cuadernos de análisis interactivo
│   ├── 01_exploracion.ipynb           # Análisis exploratorio de datos (EDA)
│   └── 02_modelo.ipynb                # Estimaciones y pruebas econométricas
├── outputs/                           # Archivos de salida generales
├── paper/                             # Minipaper académico en LaTeX / PDF
│   ├── main.tex                       # Código fuente del documento
│   └── referencias.bib                # Bibliografía en formato BibTeX
├── prompts/                           # Registro transparente de IA
│   └── registro_uso_ia.md             # Bitácora detallada de prompts
└── src/                               # Scripts de Python organizados
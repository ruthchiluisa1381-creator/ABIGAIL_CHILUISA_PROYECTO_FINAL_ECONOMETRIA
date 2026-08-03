import os
import json
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

# 1. CREAR LA ESTRUCTURA DE CARPETAS DE OUTPUTS
DIRS = [
    os.path.join("outputs", "figures"),
    os.path.join("outputs", "tables"),
    os.path.join("outputs", "results")
]

for directory in DIRS:
    os.makedirs(directory, exist_ok=True)

print("📁 Carpetas creadas o verificadas dentro de outputs/")

# 2. CARGA DE DATOS PROCESADOS
DATA_PATH = os.path.join("data", "processed", "enemdu_procesado.csv")

if not os.path.exists(DATA_PATH):
    print(f"⚠️ No se encontró {DATA_PATH}. Asegúrate de ejecutar 'limpiar_datos.py' primero.")
    exit()

df = pd.read_csv(DATA_PATH, sep=';', low_memory=False)

# --- IDENTIFICACIÓN / CREACIÓN DE VARIABLE DEPENDIENTE BINARIA (0 o 1) ---
binary_candidate = None
for col in df.select_dtypes(include=[np.number]).columns:
    unique_vals = df[col].dropna().unique()
    if set(unique_vals).issubset({0, 1, 0.0, 1.0}):
        binary_candidate = col
        break

if binary_candidate:
    y_col = binary_candidate
    df_clean = df.dropna(subset=[y_col]).copy()
else:
    num_col = df.select_dtypes(include=[np.number]).columns[0]
    y_col = f"{num_col}_binaria"
    median_val = df[num_col].median()
    df_clean = df.dropna(subset=[num_col]).copy()
    df_clean[y_col] = (df_clean[num_col] > median_val).astype(int)

# Seleccionar variables independientes continuas/numéricas
x_cols = [c for c in df_clean.select_dtypes(include=[np.number]).columns if c not in [y_col] and df_clean[c].nunique() > 1][:3]

# Limpiar nulos finales
df_clean = df_clean[[y_col] + x_cols].dropna()

X = sm.add_constant(df_clean[x_cols])
y = df_clean[y_col].astype(int)

# --- ESTIMACIÓN DE MODELOS ---
logit_mod = sm.Logit(y, X).fit(disp=0)
probit_mod = sm.Probit(y, X).fit(disp=0)

# ==========================================
# 3. GENERAR FIGURAS (outputs/figures/)
# ==========================================
sns.set_theme(style="whitegrid")

# a) curva_roc.png
prob_logit = logit_mod.predict(X)
prob_probit = probit_mod.predict(X)

fpr_l, tpr_l, _ = roc_curve(y, prob_logit)
fpr_p, tpr_p, _ = roc_curve(y, prob_probit)

plt.figure(figsize=(7, 5))
plt.plot(fpr_l, tpr_l, label=f'Logit (AUC = {roc_auc_score(y, prob_logit):.3f})', color='blue')
plt.plot(fpr_p, tpr_p, label=f'Probit (AUC = {roc_auc_score(y, prob_probit):.3f})', color='green', linestyle='--')
plt.plot([0, 1], [0, 1], color='gray', linestyle=':')
plt.title('Comparación de Curvas ROC')
plt.xlabel('1 - Especificidad')
plt.ylabel('Sensibilidad')
plt.legend()
plt.savefig(os.path.join("outputs", "figures", "curva_roc.png"), bbox_inches='tight')
plt.close()

# b) efectos_marginales.png (Ajuste robusto sin depender del nombre exacto de columna)
ame_logit = logit_mod.get_margeff(at='overall', method='dydx')
ame_summary = ame_logit.summary_frame()

# Accedemos por posición de columna: 0=dy/dx, 1=std err, 2=z, 3=p-value, 4=ci_lower, 5=ci_upper
dydx_vals = ame_summary.iloc[:, 0]
ci_lower = ame_summary.iloc[:, 4]
ci_upper = ame_summary.iloc[:, 5]

err_low = dydx_vals - ci_lower
err_high = ci_upper - dydx_vals

plt.figure(figsize=(8, 4))
plt.errorbar(
    x=ame_summary.index,
    y=dydx_vals,
    yerr=[err_low, err_high],
    fmt='o', color='darkblue', ecolor='red', capsize=5
)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title('Efectos Marginales Promedio (AME) con Intervalos de Confianza')
plt.ylabel('dy/dx')
plt.savefig(os.path.join("outputs", "figures", "efectos_marginales.png"), bbox_inches='tight')
plt.close()

# c) distribución_edad_informalidad.png
col_edad = x_cols[0] if len(x_cols) > 0 else None
if col_edad:
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=df_clean, x=col_edad, hue=y_col, common_norm=False, fill=True, palette="Set1")
    plt.title(f'Distribución de {col_edad} según Variable Dependiente')
    plt.savefig(os.path.join("outputs", "figures", "distribución_edad_informalidad.png"), bbox_inches='tight')
    plt.close()

print("✅ Gráficos guardados en outputs/figures/")

# ==========================================
# 4. GENERAR TABLAS (outputs/tables/)
# ==========================================

# a) tabla_descriptiva.csv y .tex
desc_df = df_clean.describe().T
desc_df.to_csv(os.path.join("outputs", "tables", "tabla_descriptiva.csv"))
desc_df.to_latex(os.path.join("outputs", "tables", "tabla_descriptiva.tex"))

# b) resultados_logit_probit.tex
tabla_res = pd.DataFrame({
    'Coef_Logit': logit_mod.params,
    'SE_Logit': logit_mod.bse,
    'Coef_Probit': probit_mod.params,
    'SE_Probit': probit_mod.bse
})
tabla_res.to_latex(os.path.join("outputs", "tables", "resultados_logit_probit.tex"))

# c) matriz_confusion.json y .csv
y_pred = (prob_logit >= 0.5).astype(int)
cm = confusion_matrix(y, y_pred)
cm_df = pd.DataFrame(cm, index=['Actual 0', 'Actual 1'], columns=['Pred 0', 'Pred 1'])

cm_df.to_csv(os.path.join("outputs", "tables", "matriz_confusion.csv"))
with open(os.path.join("outputs", "tables", "matriz_confusion.json"), 'w') as f:
    json.dump(cm.tolist(), f)

print("✅ Tablas guardadas en outputs/tables/")

# ==========================================
# 5. GENERAR RESULTADOS (outputs/results/)
# ==========================================

# a) resumen_modelos.txt
with open(os.path.join("outputs", "results", "resumen_modelos.txt"), "w") as f:
    f.write("=== RESUMEN MODELO LOGIT ===\n")
    f.write(logit_mod.summary().as_text())
    f.write("\n\n=== RESUMEN MODELO PROBIT ===\n")
    f.write(probit_mod.summary().as_text())

# b) metricas_json.json
metricas = {
    "logit": {
        "aic": float(logit_mod.aic),
        "bic": float(logit_mod.bic),
        "pseudo_r2": float(logit_mod.prsquared),
        "auc": float(roc_auc_score(y, prob_logit))
    },
    "probit": {
        "aic": float(probit_mod.aic),
        "bic": float(probit_mod.bic),
        "pseudo_r2": float(probit_mod.prsquared),
        "auc": float(roc_auc_score(y, prob_probit))
    }
}

with open(os.path.join("outputs", "results", "metricas_json.json"), "w") as f:
    json.dump(metricas, f, indent=4)

print("✅ Reportes y JSON guardados en outputs/results/")
print("\n🎉 ¡Todos los elementos de la carpeta outputs/ han sido generados exitosamente!")
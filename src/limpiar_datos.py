import os
import pandas as pd

# 1. Rutas de carpetas
RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

# Crear carpeta de destino si no existe
os.makedirs(PROCESSED_DIR, exist_ok=True)

# 2. Rutas de archivos
file_2024 = os.path.join(RAW_DIR, "enemdu_2024.csv")
file_2025 = os.path.join(RAW_DIR, "enemdu_2025.csv")

# Función a prueba de errores para cargar CSVs de ENEMDU
def cargar_csv_robustamente(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f"⚠️ No se encontró el archivo: {ruta_archivo}")
        return None
    
    # Probar combinaciones habituales de delimitadores y encodings
    separadores = [';', ',', '\t']
    encodings = ['latin-1', 'utf-8', 'iso-8859-1']

    for sep in separadores:
        for enc in encodings:
            try:
                df = pd.read_csv(
                    ruta_archivo, 
                    sep=sep, 
                    encoding=enc, 
                    low_memory=False, 
                    on_bad_lines='skip'  # Omite líneas dañadas si existen
                )
                # Si se lee correctamente con más de 1 columna, es el formato correcto
                if df.shape[1] > 1:
                    print(f"  ✓ Leído exitosamente: {os.path.basename(ruta_archivo)} (Separador: '{sep}', Encoding: '{enc}')")
                    return df
            except Exception:
                continue

    # Último recurso usando motor python
    try:
        return pd.read_csv(ruta_archivo, sep=None, engine='python', on_bad_lines='skip')
    except Exception as e:
        print(f"❌ Error crítico al leer {ruta_archivo}: {e}")
        return None

def ejecutar_pipeline():
    print("🔄 Cargando y limpiando datos ENEMDU 2024 y 2025...")

    # Cargar bases
    df_2024 = cargar_csv_robustamente(file_2024)
    df_2025 = cargar_csv_robustamente(file_2025)

    if df_2024 is None and df_2025 is None:
        print("❌ Error: No se pudo cargar ninguno de los dos archivos.")
        return

    # Añadir columna identificadora de año
    if df_2024 is not None:
        df_2024['anio_periodo'] = 2024
    if df_2025 is not None:
        df_2025['anio_periodo'] = 2025

    # Unir ambas bases de datos
    bases_a_unir = [df for df in [df_2024, df_2025] if df is not None]
    df_final = pd.concat(bases_a_unir, ignore_index=True)

    # 3. Guardar en data/processed
    output_path = os.path.join(PROCESSED_DIR, "enemdu_procesado.csv")
    df_final.to_csv(output_path, index=False, sep=';', encoding='utf-8')

    print(f"\n✅ ¡Proceso completado!")
    print(f"📊 Filas totales procesadas: {len(df_final)}")
    print(f"📁 Archivo guardado en: {output_path}")

if __name__ == "__main__":
    ejecutar_pipeline()
    
    
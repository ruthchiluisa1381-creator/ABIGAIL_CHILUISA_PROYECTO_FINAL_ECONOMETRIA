import os

def verificar_datos():
    """Comprueba que las bases de la ENEMDU 2024 y 2025 existan en data/raw/."""
    archivos = os.listdir("data/raw")
    print(f"Archivos encontrados en data/raw/: {archivos}")
    if not archivos:
        print("⚠️ Advertencia: Agrega los archivos de la ENEMDU 2024 y 2025 dentro de 'data/raw/'")

if __name__ == "__main__":
    verificar_datos()
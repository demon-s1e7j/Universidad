from mp_api.client import MPRester
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Configura tu API Key
API_KEY = os.getenv("MATERIALS_PROJECT_API_KEY")

def obtener_absolutamente_todo():
    print("Conectando con Materials Project...")
    
    with MPRester(API_KEY) as mpr:
        # 1. Filtramos: Queremos TODOS los materiales que tengan datos dieléctricos
        # Al no poner 'fields', la API descargará TODAS las columnas existentes.
        print("Descargando la base de datos completa (esto puede tardar unos segundos)...")
        docs = mpr.materials.summary.search(has_props=["dielectric"])
    
    print(f"¡Se descargaron {len(docs)} materiales!")
    
    # 2. Convertimos los objetos (Pydantic models) a diccionarios nativos de Python
    # 'model_dump()' extrae absolutamente todos los datos del material
    datos = [doc.model_dump() for doc in docs]
    
    # 3. Creamos el DataFrame
    df = pd.DataFrame(datos)
    
    print(f"El DataFrame tiene {len(df.columns)} columnas de información.")
    
    # 4. Limpieza de seguridad para Excel
    # La API devuelve tensores y listas anidadas. Excel odia las listas en las celdas, 
    # así que convertimos cualquier lista o diccionario a texto para que no de error al guardar.
    df = df.apply(lambda col: col.map(lambda x: str(x) if isinstance(x, (list, dict)) else x))
    
    # 5. Exportamos
    print("Exportando a CSV y Excel...")
    df.to_csv("dielectricos_absolutamente_todo.csv", index=False)
    df.to_excel("dielectricos_absolutamente_todo.xlsx", index=False)
    
    print("¡Listo! Tienes todo el conocimiento de MP en tus archivos.")

if __name__ == "__main__":
    obtener_absolutamente_todo()

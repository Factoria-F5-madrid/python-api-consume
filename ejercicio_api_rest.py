"""
Ejercicio básico: consumir una API REST en Python vanilla (sin librerías externas)

Usamos urllib (viene con Python) para:
  1. Hacer un GET a una API pública real y ver los datos que devuelve
  2. Guardar esos datos en un archivo .json
  3. Leer el .json y mostrarlo
  4. Añadir un dato nuevo al .json (a mano, sin servidor)

TU TAREA: completa cada # TODO
"""

import json
import urllib.request

API_URL = "https://jsonplaceholder.typicode.com/todos/1"
ARCHIVO = "datos.json"

# ---------- 1. GET a la API ----------
# TODO 1: haz la petición y carga la respuesta como JSON (dict de Python)
# Pista:
#   with urllib.request.urlopen(API_URL) as respuesta:
#       datos = json.load(respuesta)
datos = None

print("Datos recibidos de la API:")
print(datos)

# ---------- 2. Guardar en un archivo .json ----------
# TODO 2: guarda `datos` en ARCHIVO con json.dump
# Pista:
#   with open(ARCHIVO, "w", encoding="utf-8") as f:
#       json.dump(datos, f, indent=2, ensure_ascii=False)

# ---------- 3. Leer el archivo y mostrarlo ----------
# TODO 3: abre ARCHIVO, cárgalo con json.load y guárdalo en `datos_leidos`
# Pista:
#   with open(ARCHIVO, encoding="utf-8") as f:
#       datos_leidos = json.load(f)
datos_leidos = None

print("\nDatos leídos del archivo:")
print(datos_leidos)

# ---------- 4. Añadir un campo nuevo y volver a guardar ----------
# TODO 4: añade una clave nueva a datos_leidos (ej: datos_leidos["revisado"] = True)
# y vuelve a guardarlo en ARCHIVO igual que en el TODO 2

print("\nListo. Revisa el archivo", ARCHIVO)

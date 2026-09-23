# Ejercicio: leer una API REST en Python vanilla

Ejercicio básico para practicar cómo consumir una API REST desde Python usando
**solo la librería estándar** (`urllib` y `json`, nada que instalar con `pip`).

Vas a completar `ejercicio_api_rest.py`, que tiene 4 partes marcadas con `# TODO`.
Cada una explicada abajo, con el código exacto que hay que escribir y qué hace cada línea.

## Requisitos

- Python 3 instalado.
- Conexión a internet (vamos a llamar a una API real).

## Paso 0 — Entiende el archivo

Al principio del script hay dos constantes:

```python
API_URL = "https://jsonplaceholder.typicode.com/todos/1"
ARCHIVO = "datos.json"
```

- `API_URL` es el **endpoint**: la URL a la que le vamos a pedir datos. Es una API pública
  gratuita que no necesita clave ni login, pensada para practicar.
- `ARCHIVO` es el nombre del archivo local donde vamos a guardar lo que recibamos.

## Paso 1 — TODO 1: pedir los datos a la API (GET)

Busca esta parte del archivo:

```python
# ---------- 1. GET a la API ----------
# TODO 1: haz la petición y carga la respuesta como JSON (dict de Python)
datos = None
```

Sustituye `datos = None` por:

```python
with urllib.request.urlopen(API_URL) as respuesta:
    datos = json.load(respuesta)
```

**Qué hace cada línea:**

- `urllib.request.urlopen(API_URL)` — abre una conexión HTTP y hace un **GET** a esa URL
  (el método por defecto de `urlopen`). Es lo mismo que pasa cuando escribes una URL en el
  navegador: le pides al servidor "dame lo que tengas en esta dirección".
- `with ... as respuesta:` — abre la conexión y la cierra sola al terminar el bloque
  (evita tener que acordarte de cerrarla a mano).
- `json.load(respuesta)` — la API devuelve el cuerpo de la respuesta en formato JSON (texto).
  `json.load` lee ese texto y lo convierte en un **diccionario de Python** con el que ya
  puedes trabajar normal (`datos["title"]`, etc.).
- `datos = ...` — guardamos ese diccionario en la variable `datos`.

Guarda el archivo y ejecuta:

```bash
python ejercicio_api_rest.py
```

Deberías ver algo como:

```
Datos recibidos de la API:
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
```

## Paso 2 — TODO 2: guardar los datos en un archivo `.json`

Busca:

```python
# ---------- 2. Guardar en un archivo .json ----------
# TODO 2: guarda `datos` en ARCHIVO con json.dump
```

Debajo, añade:

```python
with open(ARCHIVO, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
```

**Qué hace cada línea:**

- `open(ARCHIVO, "w", encoding="utf-8")` — abre (o crea si no existe) el archivo `datos.json`
  en modo escritura (`"w"`). `encoding="utf-8"` evita problemas con tildes/ñ.
- `json.dump(datos, f, ...)` — convierte el diccionario `datos` a texto JSON y lo escribe
  dentro del archivo `f`.
- `indent=2` — formatea el JSON con sangría de 2 espacios, para que sea legible al abrirlo
  (si no, saldría todo en una sola línea).
- `ensure_ascii=False` — permite guardar tildes/ñ tal cual, en vez de como códigos raros tipo `ñ`.

Ejecuta de nuevo el script y comprueba que se ha creado el archivo `datos.json` en la misma carpeta. Ábrelo con cualquier editor de texto.

## Paso 3 — TODO 3: leer el archivo `.json`

Busca:

```python
# ---------- 3. Leer el archivo y mostrarlo ----------
# TODO 3: abre ARCHIVO, cárgalo con json.load y guárdalo en `datos_leidos`
datos_leidos = None
```

Sustituye `datos_leidos = None` por:

```python
with open(ARCHIVO, encoding="utf-8") as f:
    datos_leidos = json.load(f)
```

**Qué hace cada línea:**

- `open(ARCHIVO, encoding="utf-8")` — abre el archivo en modo lectura (por defecto, no hace
  falta poner `"r"`).
- `json.load(f)` — lee el contenido del archivo (que es texto JSON) y lo convierte de nuevo
  en un diccionario de Python. Es la operación inversa a `json.dump`.

Al ejecutar el script verás los mismos datos, pero esta vez vienen del archivo, no de la API.

## Paso 4 — TODO 4: modificar el JSON y volver a guardarlo

Busca:

```python
# ---------- 4. Añadir un campo nuevo y volver a guardar ----------
# TODO 4: añade una clave nueva a datos_leidos (ej: datos_leidos["revisado"] = True)
# y vuelve a guardarlo en ARCHIVO igual que en el TODO 2
```

Debajo, añade:

```python
datos_leidos["revisado"] = True

with open(ARCHIVO, "w", encoding="utf-8") as f:
    json.dump(datos_leidos, f, indent=2, ensure_ascii=False)
```

**Qué hace cada línea:**

- `datos_leidos["revisado"] = True` — un diccionario de Python se modifica como cualquier
  `dict`: `diccionario["clave_nueva"] = valor`. Esto añade la clave `"revisado"` con valor
  `True` (si ya existiera, la sobrescribiría).
- El bloque `with open(...)` es exactamente el mismo que en el Paso 2: volvemos a escribir
  el diccionario (ya modificado) en el archivo, sobrescribiéndolo.

## Paso 5 — Verificación final

Ejecuta el script una última vez:

```bash
python ejercicio_api_rest.py
```

Y abre `datos.json`. Debe verse así (los valores pueden variar):

```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false,
  "revisado": true
}
```

Si aparece el campo `"revisado": true`, el ejercicio está completo.

## ¿Te atascas?

Compara con `solucion_api_rest.py`, que tiene los 4 TODOs ya resueltos.

## Resumen de conceptos usados

| Concepto | En el código |
|---|---|
| Endpoint (URL de la API) | `API_URL` |
| Petición GET | `urllib.request.urlopen(API_URL)` |
| Respuesta en formato JSON | `json.load(respuesta)` |
| Guardar un dict como JSON en disco | `json.dump(datos, f, ...)` |
| Leer un JSON de disco | `json.load(f)` |
| Modificar un diccionario en Python | `datos_leidos["clave"] = valor` |

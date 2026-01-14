"""
API REST con FastAPI y Supabase
"""

from fastapi import FastAPI, HTTPException
from Modelos.persona import Persona
from Modelos.caja_dto import Caja
from db.client_supabase import supabase  # Cliente global de Supabase

# Base de datos temporal para personas
dbPersona = []

# Descripción completa de la API con Markdown

description = """

## 🎓 API REST de cajas - UTPL

Esta API REST fue desarrollada con **FastAPI** para enseñar a estudiantes los conceptos fundamentales 

de desarrollo de APIs modernas y la interoperabilidad de sistemas.

### 📋 Funcionalidades principales

#### Gestión de cajas

Puedes realizar operaciones CRUD completas:

* **Crear** nuevas cajas con validación de datos

* **Consultar** todas las cajas o buscar por identificación

* **Actualizar** información de cajas existentes

* **Eliminar** registros de cajas

#### Base de Datos

* Integración con **Supabase** como backend

* Validación automática de datos con Pydantic

* Manejo de errores HTTP

### 👨‍🏫 Información del Curso

**Materia:** Interoperabilidad Empresarial 

**Institución:** Universidad Técnica Particular de Loja (UTPL)  

**Email:** daamores2@utpl.edu.ec  

### 🚀 Tecnologías

* FastAPI 

* Python 3.8+

* Supabase

* Pydantic para validación de datos

"""

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de gestion de cajas",
    description=description,
    version="1.0.0"
)

# -------------------------
#   CAJAS (CRUD en Supabase)
# -------------------------
@app.post("/cajas", response_model=Caja, tags=["Cajas"])
def crear_caja(caja: Caja):
    response = supabase.table("cajas").insert(caja.dict()).execute()
    if response.data is None:
        raise HTTPException(status_code=500, detail="No se pudo crear la caja en la base de datos")
    return caja

@app.get("/cajas", response_model=list[Caja], tags=["Cajas"])
def obtener_cajas():
    response = supabase.table("cajas").select("*").execute()
    return [Caja(**item) for item in response.data]

@app.get("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def obtener_caja_por_id(id: str):
    response = supabase.table("cajas").select("*").eq("id", id).single().execute()
    if response.data is None:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    return Caja(**response.data)

@app.put("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def actualizar_caja(id: str, caja_actualizada: Caja):
    if caja_actualizada.id != id:
        raise HTTPException(status_code=400, detail="El ID de la caja no coincide con la ruta")
    response = supabase.table("cajas").update(caja_actualizada.dict()).eq("id", id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    return caja_actualizada

@app.delete("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def eliminar_caja(id: str):
    response_get = supabase.table("cajas").select("*").eq("id", id).single().execute()
    if response_get.data is None:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    supabase.table("cajas").delete().eq("id", id).execute()
    return Caja(**response_get.data)

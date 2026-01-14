"""
API REST con FastAPI
Incluye personas (local) y cajas (Supabase)
"""

from fastapi import FastAPI, HTTPException
from Modelos.persona import Persona
from Modelos.caja_dto import Caja
from db.client_supabase import supabase  # Cliente global de Supabase

# BASE DE DATOS LOCAL TEMPORAL (personas)
dbPersona = []

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - daamores2@utpl.edu.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)

# -------------------------
# RUTAS GENERALES
# -------------------------

@app.get("/")
def root():
    return {"mensaje": "¡Hola Mundo desde FastAPI por David!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"¡Hola {nombre}! Bienvenido a la API"}

@app.get("/info")
def informacion():
    return {
        "nombre": "API de Ejemplo UTPL",
        "version": "1.0.0",
        "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
    }

# -------------------------
# PERSONAS (CRUD local)
# -------------------------

@app.post("/personas", response_model=Persona, tags=["Personas"])
def crear_persona(persona: Persona):
    dbPersona.append(persona)
    return persona

@app.get("/personas", response_model=list[Persona], tags=["Personas"])
def obtener_personas():
    return dbPersona

@app.get("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def obtener_persona_por_identificacion(identificacion: str):
    for persona in dbPersona:
        if persona.identificacion == identificacion:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.put("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def actualizar_persona(identificacion: str, persona_actualizada: Persona):
    if persona_actualizada.identificacion != identificacion:
        raise HTTPException(status_code=400, detail="La identificación del cuerpo no coincide con la ruta")

    for idx, persona in enumerate(dbPersona):
        if persona.identificacion == identificacion:
            dbPersona[idx] = persona_actualizada
            return persona_actualizada

    raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.delete("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def eliminar_persona(identificacion: str):
    for idx, persona in enumerate(dbPersona):
        if persona.identificacion == identificacion:
            return dbPersona.pop(idx)
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# -------------------------
# CAJAS (CRUD con Supabase)
# -------------------------


@app.post("/cajas", response_model=Caja, tags=["Cajas"])
def crear_caja(caja: Caja):
    response = supabase.table("cajas").insert(caja.dict()).execute()
    if response.status_code != 201:
        raise HTTPException(status_code=400, detail="No se pudo crear la caja")
    return caja

@app.get("/cajas", response_model=list[Caja], tags=["Cajas"])
def obtener_cajas():
    response = supabase.table("cajas").select("*").execute()
    return response.data or []

@app.get("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def obtener_caja_por_id(id: str):
    response = supabase.table("cajas").select("*").eq("id", id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    return response.data[0]

@app.put("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def actualizar_caja(id: str, caja_actualizada: Caja):
    # Verificar que el ID del body coincida con el de la ruta
    if caja_actualizada.id != id:
        raise HTTPException(status_code=400, detail="El ID del cuerpo no coincide con la ruta")

    # Actualizar en Supabase
    response = supabase.table("cajas").update(caja_actualizada.dict()).eq("id", id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    return response.data[0]

@app.delete("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def eliminar_caja(id: str):
    # Primero obtener la caja para devolverla luego
    response = supabase.table("cajas").select("*").eq("id", id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    
    caja_a_eliminar = response.data[0]

    # Eliminar la caja
    supabase.table("cajas").delete().eq("id", id).execute()
    
    return caja_a_eliminar
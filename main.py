"""
API REST básica con FastAPI
Este es un esqueleto de API para enseñar a estudiantes
"""

from fastapi import FastAPI, HTTPException
from Modelos.persona import Persona
from Modelos.caja_dto import Caja

# BASES DE DATOS TEMPORALES (listas)
dbPersona = []
dbCaja = []

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - fdquinones@utpl.edu.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"mensaje": "¡Hola Mundo desde FastAPI por Felipe!"}

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
#   PERSONAS (CRUD)
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
#   CAJAS (CRUD)
# -------------------------

@app.post("/cajas", response_model=Caja, tags=["Cajas"])
def crear_caja(caja: Caja):
    dbCaja.append(caja)
    return caja

@app.get("/cajas", response_model=list[Caja], tags=["Cajas"])
def obtener_cajas():
    return dbCaja

@app.get("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def obtener_caja_por_id(id: str):
    for caja in dbCaja:
        if caja.id == id:
            return caja
    raise HTTPException(status_code=404, detail="Caja no encontrada")

@app.put("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def actualizar_caja(id: str, caja_actualizada: Caja):
    if caja_actualizada.id != id:
        raise HTTPException(status_code=400, detail="El ID del cuerpo no coincide con la ruta")

    for idx, caja in enumerate(dbCaja):
        if caja.id == id:
            dbCaja[idx] = caja_actualizada
            return caja_actualizada
    raise HTTPException(status_code=404, detail="Caja no encontrada")

@app.delete("/cajas/{id}", response_model=Caja, tags=["Cajas"])
def eliminar_caja(id: str):
    for idx, caja in enumerate(dbCaja):
        if caja.id == id:
            return dbCaja.pop(idx)
    raise HTTPException(status_code=404, detail="Caja no encontrada")

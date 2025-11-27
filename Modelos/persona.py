from pydantic import BaseModel, EmailStr, Field

class Persona(BaseModel):

    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la persona")
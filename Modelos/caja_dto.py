from pydantic import BaseModel, Field


class Caja(BaseModel):
    id: str = Field(..., description="Identificador único de la caja")
    peso: float = Field(..., gt=0, description="Peso en kg")
    color: str = Field(..., min_length=1, max_length=50, description="Color de la caja")
    material: str = Field(..., min_length=1, max_length=100, description="Material de la caja")
    capacidad: float = Field(..., gt=0, description="Capacidad máxima en kg")
    descripcion: str | None = Field(None, description="Descripción opcional")

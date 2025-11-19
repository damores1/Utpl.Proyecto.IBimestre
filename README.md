# Utpl.Proyecto.IBimestre
Repositorio base del proyecto de 1 primestre de Interoperabilidad por David Amores. daamores2@utpl.edu.ec

## Descripción
Este proyecto contiene una API REST básica desarrollada con FastAPI para propósitos educativos. El objetivo es enseñar cómo trabajar con APIs REST utilizando Python y FastAPI.

## Estructura del Proyecto
```
.
├── main.py              # Archivo principal con la aplicación FastAPI
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

## Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/fdquinones1986/Utpl.Proyecto.IBimestre.git
cd Utpl.Proyecto.IBimestre
```

### 2. Crear un entorno virtual con CodeSpace

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## Inicializar la API

### Ejecutar el servidor de desarrollo
```bash
uvicorn main:app --reload
```

El servidor se iniciará en `http://127.0.0.1:8000`

### Opciones adicionales
- **Puerto personalizado:** `uvicorn main:app --reload --port 8080`
- **Host público:** `uvicorn main:app --reload --host 0.0.0.0`

## Endpoints Disponibles

Una vez que la API esté corriendo, puedes probar los siguientes endpoints:

### 1. Hola Mundo
```
GET http://127.0.0.1:8000/
```
Respuesta:
```json
{
  "mensaje": "¡Hola Mundo desde FastAPI!"
}
```

### 2. Saludo personalizado
```
GET http://127.0.0.1:8000/saludo/Juan
```
Respuesta:
```json
{
  "mensaje": "¡Hola Juan! Bienvenido a la API"
}
```

### 3. Información de la API
```
GET http://127.0.0.1:8000/info
```
Respuesta:
```json
{
  "nombre": "API de Ejemplo UTPL",
  "version": "1.0.0",
  "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
}
```

## Documentación Interactiva

FastAPI genera automáticamente documentación interactiva para tu API:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Estas interfaces te permiten probar los endpoints directamente desde el navegador.

## Próximos Pasos

Este es un esqueleto básico. Puedes expandir la API agregando:
- Más endpoints
- Modelos de datos con Pydantic
- Conexión a bases de datos
- Autenticación y autorización
- Manejo de errores personalizado
- Validación de datos
- CORS (Cross-Origin Resource Sharing)

## Recursos Adicionales
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial de FastAPI en español](https://fastapi.tiangolo.com/es/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)



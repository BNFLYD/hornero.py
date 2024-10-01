# Hornero

Este proyecto es una aplicación web desarrollada con FastAPI y SQLAlchemy.

## Requisitos previos

* Python 3.9 o superior
* pip (el gestor de paquetes de Python)
* Un entorno de desarrollo de Python (recomendado: PyCharm, Visual Studio Code, etc.)

## Inicialización del proyecto

### 1. Clonar el repositorio

Clona el repositorio en tu máquina local ejecutando el siguiente comando en la terminal:

```bash
git clone https://github.com/tu-usuario/hornero.git
```

### 2. Instalar las dependencias
Instala las dependencias del proyecto ejecutando el siguiente comando en la terminal:

```bash
pip install -r requirements.txt
```

### 3. Configurar la base de datos
Crea un archivo .env en la raíz del proyecto con las siguientes variables de entorno:

makefile
POSTGRES_USER=tu-usuario
POSTGRES_PASSWORD=tu-contraseña
POSTGRES_DB=tu-base-de-datos
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

### 4. Crear la base de datos
Crea la base de datos ejecutando el siguiente comando en la terminal:

```bash
alembic upgrade head
```
### 5. Iniciar la aplicación
Inicia la aplicación ejecutando el siguiente comando en la terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
La aplicación estará disponible en http://localhost:8000.

## Desarrollo
Para desarrollar la aplicación, ejecuta el siguiente comando en la terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Esto iniciará la aplicación en modo de desarrollo, que se recargará automáticamente cuando se realicen cambios en el código.

## Pruebas
Para ejecutar las pruebas, ejecuta el siguiente comando en la terminal:

```bash
pytest
```
Esto ejecutará todas las pruebas del proyecto.

## Documentación
La documentación de la API está disponible en http://localhost:8000/docs.

Espero que esto te ayude a inicializar el proyecto. Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en preguntar.

## Contenedores 

El contenedor de postgres se ejecuta en segundo plano tomando en cuenta las variables de entorno 
```docker
docker run --name postgres -d -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=*** postgres
```
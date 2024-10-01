# Utilizamos la imagen oficial de Python como base
FROM python:3.12.5-slim

# Establecemos la variable de entorno para el nombre de la base de datos
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=***

# Instalamos las dependencias de Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación
COPY . /app

# Establecemos la variable de entorno para la configuración de la base de datos
ENV DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/$POSTGRES_DB

# Exponemos el puerto 8000 para que se pueda acceder a la API
EXPOSE 8000

# Inicializamos el servicio de FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
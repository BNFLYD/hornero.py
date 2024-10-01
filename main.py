from fastapi import Depends, FastAPI, Request, Response
from config.db import create_diagram

create_diagram()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola gil esto es una prueba"}

@app.middleware("http")
async def ignore_favicon(request: Request, call_next):
    if request.url.path == "/favicon.ico":
        return Response(status_code=204)
    return await call_next(request)
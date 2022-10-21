
#importando funciones de fastapi y las rutas
from ensurepip import version
from turtle import title
from fastapi import FastAPI
from rutas.user import user

app = FastAPI(
    title="Funcionamiento de fastapi",
    description="Se muestra como funciona",
    version="1.0",
    openapi_tags=[{
        "name":"usuarios",
        "description":"rutas de usuarios"
    }]
)

app.include_router(user)

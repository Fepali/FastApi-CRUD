#importando funciones
from distutils.command.build_scripts import first_line_re
from pyexpat import model
from urllib import response
from fastapi import APIRouter, Response, status
from configuracion.db import conn
from modelos.user import usuarios 
from esquemas.user import User
from starlette.status import  HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

#función para encriptar contraseña
key = Fernet.generate_key()
fun = Fernet(key)

#funcion que hace que funcionen las rutas
user = APIRouter()

#consulta a todos los usuarios
@user.get("/users", response_model=list[User], tags=["Usuarios"])
def get_users():
    return conn.execute(usuarios.select()).fetchall()

#agregar usuario
@user.post("/users", response_model=User, tags=["Usuarios"])
def create_user(user: User):
    new_user = {"nombre": user.nombre, "email": user.email}
    new_user["contraseña"] = fun.encrypt(user.contraseña.encode("utf-8"))
    result = conn.execute(usuarios.insert().values(new_user))
    return conn.execute(usuarios.select().where(usuarios.c.id == result.lastrowid)).first()

#consultar usuario
@user.get("/users/{id}", response_model=User, tags=["Usuarios"])
def get_user(id: str):
    return conn.execute(usuarios.select().where(usuarios.c.id == id)).first()

#eliminar usuario
@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def delete_user(id: str):
    conn.execute(usuarios.delete().where(usuarios.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

#actualizar usuario
@user.put("/users/{id}", response_model=User, tags=["Usuarios"])
def update_user(id: str, user: User):
    conn.execute(usuarios.update().values(nombre=user.nombre, 
                email=user.email, 
                contraseña=fun.encrypt(user.contraseña.encode("utf-8"))
    ).where(usuarios.c.id == id))
    return conn.execute(usuarios.select().where(usuarios.c.id == id)).first()
from tokenize import String
#importando funciones de sqlalchemy y de la configuracion de la base de datos
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from configuracion.db import meta,engine

#creando la tabla usuarios
usuarios = Table("usuarios", meta, Column(
    "id", Integer, primary_key=True), 
    Column("nombre", String(255)),
    Column("email", String(255)),
    Column("contraseña", String(255)))

meta.create_all(engine)

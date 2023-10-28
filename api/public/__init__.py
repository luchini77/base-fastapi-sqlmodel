from fastapi import APIRouter

from api.public.usuario import views as usuarios
from api.public.tareas import views as tareas


api = APIRouter()


api.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
api.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])
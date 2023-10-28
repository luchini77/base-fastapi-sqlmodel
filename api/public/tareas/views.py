from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from api.database import get_session
from api.public.tareas.models import TareaCrear, TareaLeer, TareaActualizar
from api.public.tareas.crud import (get_tareas, create_tarea, get_by_id, update_tarea, delete_tarea, get_tareas_usuario)


router = APIRouter()


@router.get("", response_model=List[TareaLeer])
def leer_tareas(db:Session=Depends(get_session)):
    return get_tareas(db=db)


@router.get("/{usuario_id}", response_model=List[TareaLeer])
def leer_tareas_usuario(usuario_id:int,db:Session=Depends(get_session)):
    return get_tareas_usuario(usuario_id=usuario_id,db=db)


@router.post("", response_model=TareaLeer)
def crear_tarea(tarea:TareaCrear,db:Session=Depends(get_session)):
    return create_tarea(tarea=tarea, db=db)


@router.get("/{id}", response_model=TareaLeer)
def leer_tarea(id:int,db:Session=Depends(get_session)):
    return get_by_id(id=id,db=db)


@router.patch("/{id}", response_model=TareaLeer)
def actualizar_tarea(id:int,tarea:TareaActualizar,db:Session=Depends(get_session)):
    return update_tarea(id=id, tarea=tarea,db=db)


@router.delete("/{id}")
def borrar_tarea(id:int,db:Session=Depends(get_session)):
    return delete_tarea(id=id,db=db)
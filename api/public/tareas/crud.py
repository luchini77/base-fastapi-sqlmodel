from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.tareas.models import Tarea, TareaCrear, TareaActualizar


def get_tareas(db:Session=Depends(get_session)):
    tareas = db.exec(select(Tarea)).all()
    return tareas


def get_tareas_usuario(usuario_id:int,db:Session=Depends(get_session)):
    tareas = db.exec(select(Tarea).where(Tarea.usuario_id == usuario_id)).all()

    if not tareas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra tareas del usuario: {usuario_id}')

    return tareas


def create_tarea(tarea:TareaCrear, db:Session=Depends(get_session)):
    new_tarea = Tarea.from_orm(tarea)
    db.add(new_tarea)
    db.commit()
    db.refresh(new_tarea)
    return new_tarea


def get_by_id(id:int,db:Session=Depends(get_session)):
    tarea = db.get(Tarea,id)

    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra tarea con ese id: {id}')

    return tarea


def update_tarea(id:int,tarea:TareaActualizar,db:Session=Depends(get_session)):
    tarea_update = db.get(Tarea,id)

    if not tarea_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra tarea con ese id: {id}')

    tarea_data = tarea.dict(exclude_unset=True)

    for key,value in tarea_data.items():
        setattr(tarea_update,key,value)

    db.add(tarea_update)
    db.commit()
    db.refresh(tarea_update)
    return tarea_update


def delete_tarea(id:int,db:Session=Depends(get_session)):
    tarea = db.get(Tarea,id)

    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra tarea con ese id: {id}')

    db.delete(tarea)
    db.commit()
    return {"OK":True}
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.usuario.models import Usuario, UsuarioCrear, UsuarioActualizar


def get_users(db:Session=Depends(get_session)):
    usuarios = db.exec(select(Usuario)).all()
    return usuarios


def create_user(usuario:UsuarioCrear, db:Session=Depends(get_session)):
    new_usuario = Usuario.from_orm(usuario)
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    return new_usuario


def get_by_id(id:int,db:Session=Depends(get_session)):
    usuario = db.get(Usuario,id)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra usuario con ese id: {id}')

    return usuario


def update_user(id:int,usuario:UsuarioActualizar,db:Session=Depends(get_session)):
    usuario_update = db.get(Usuario,id)

    if not usuario_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra usuario con ese id: {id}')

    usuario_data = usuario.dict(exclude_unset=True)

    for key,value in usuario_data.items():
        setattr(usuario_update,key,value)

    db.add(usuario_update)
    db.commit()
    db.refresh(usuario_update)
    return usuario_update


def delete_user(id:int,db:Session=Depends(get_session)):
    usuario = db.get(Usuario,id)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra usuario con ese id: {id}')

    db.delete(usuario)
    db.commit()
    return {"OK":True}
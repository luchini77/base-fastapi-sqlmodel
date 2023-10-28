from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from api.database import get_session
from api.public.usuario.models import UsuarioCrear, UsuarioLeer, UsuarioActualizar
from api.public.usuario.crud import (get_users, create_user, get_by_id, update_user, delete_user)


router = APIRouter()


@router.get("", response_model=List[UsuarioLeer])
def leer_usuarios(db:Session=Depends(get_session)):
    return get_users(db=db)


@router.post("", response_model=UsuarioLeer)
def crear_usuario(usuario:UsuarioCrear,db:Session=Depends(get_session)):
    return create_user(usuario=usuario, db=db)


@router.get("/{id}", response_model=UsuarioLeer)
def leer_usuario(id:int,db:Session=Depends(get_session)):
    return get_by_id(id=id,db=db)


@router.patch("/{id}", response_model=UsuarioLeer)
def actualizar_usuario(id:int,usuario:UsuarioActualizar,db:Session=Depends(get_session)):
    return update_user(id=id, usuario=usuario,db=db)


@router.delete("/{id}")
def borrar_usuario(id:int,db:Session=Depends(get_session)):
    return delete_user(id=id,db=db)
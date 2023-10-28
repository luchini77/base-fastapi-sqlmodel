from typing import Optional
from sqlmodel import Field, Relationship, SQLModel 

from api.public.usuario.models import Usuario


class TareaBase(SQLModel):
    titulo: str
    contenido: str
    terminada: bool
    usuario_id: int


    class Config:
        schema_extra = {
            "example": {
                "titulo":"Laar",
                "contenido":"Y bien laaooo",
                "terminada":False,
                "usuario_id": 1
            }
        }


class Tarea(TareaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: Optional[int] = Field(default=None,foreign_key="usuario.id")
    usuario: Optional[Usuario] = Relationship(back_populates="tareas")



class TareaCrear(TareaBase):
    pass


class TareaLeer(TareaBase):
    id: int
    titulo: Optional[str] = None
    contenido: Optional[str] = None
    usuario_id: Optional[int] = None


class TareaActualizar(TareaBase):
    titulo: Optional[str] = None
    contenido: Optional[str] = None
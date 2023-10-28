from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel 



class UsuarioBase(SQLModel):
    nombre: str


    class Config:
        schema_extra = {
            "example": {
                "nombre":"Alberta"
            }
        }


class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    tareas: List["Tarea"] = Relationship(back_populates="usuario")


class UsuarioCrear(UsuarioBase):
    pass


class UsuarioLeer(UsuarioBase):
    id: int
    nombre: Optional[str] = None


class UsuarioActualizar(UsuarioBase):
    nombre: Optional[str] = None
from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Optional, List

class Livro(BaseModel):

    ref_id: Optional[str]= None
    id: int
    nome: str
    editora: str
    autor: str
    descricao:str
    foto: str
from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base


class Livro(Base):
    __tablename__ = "Livro"

    ref_id = Column(Integer, primary_key=True, index=True)
    id = Column (Integer)
    nome = Column(String)
    editora = Column(String)
    descricao = Column(String)
    foto = Column(String)

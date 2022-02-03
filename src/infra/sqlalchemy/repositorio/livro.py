from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioLivro():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, livro:schemas.Livro):
        db_livros = models.Livro(  id = livro.id,
                                   nome = livro.nome,
                                   editora = livro.editora,
                                   autor = livro.autor,
                                   descricao = livro.descricao,
                                   foto = livro.foto )


        self.db.add(db_livros)
        self.db.commit()
        self.db.refresh(db_livros)
        return db_livros


    def listar(self):
        livros = self.db.query(models.Produto).all()
        return livros


    def obter (self):
        ...
    def remover(self):
        ...


import sqlalchemy as sa
from datetime import datetime
from .model_base import ModelBase


class Conservantes(ModelBase):
    __tablename__: str = "conservantes"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)
    descricao: str = sa.Column(sa.String(45), nullable=False)

    def __str__(self) -> str:
        return f"<Conservantes: {self.nome}>"

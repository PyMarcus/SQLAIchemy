import sqlalchemy as sa
from datetime import datetime
from .model_base import ModelBase


class TiposEmbalagens(ModelBase):
    __tablename__: str = "tipos_embalagens"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)

    def __str__(self) -> str:
        return f"<TiposEmbalagens: {self.nome}>"

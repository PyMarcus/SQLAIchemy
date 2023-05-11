import sqlalchemy as sa
from datetime import datetime
from .model_base import ModelBase


class Revendedores(ModelBase):
    __tablename__: str = "revendedores"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    cnpj: str = sa.Column(sa.String(45), nullable=False, unique=True)
    razao_social: str = sa.Column(sa.String(100), nullable=False, unique=True)
    contato: str = sa.Column(sa.String(100))

    def __str__(self) -> str:
        return f"<Revendedores: {self.nome}>"

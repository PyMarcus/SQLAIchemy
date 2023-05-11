import sqlalchemy as sa
from datetime import datetime
from .model_base import ModelBase


class AditivoNutritivo(ModelBase):
    __tablename__: str = "aditivos_nutritivos"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    formula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<AditivoNutritivo: {self.nome}>"

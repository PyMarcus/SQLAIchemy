import sqlalchemy as sa
from datetime import datetime
from model_base import ModelBase


class ConservantesPicole(ModelBase):
    __tablename__: str = "conservantes_picole"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_conservante: int = sa.Column(sa.Integer, sa.ForeignKey("conservantes.id"))
    id_picole: int = sa.Column(sa.Integer, sa.ForeignKey("picoles.id"))

    def __str__(self) -> str:
        return f"<ConservantesPicole: {self.nome}>"

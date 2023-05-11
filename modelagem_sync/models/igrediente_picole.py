import sqlalchemy as sa
from datetime import datetime
from model_base import ModelBase


class IgredientesPicole(ModelBase):
    __tablename__: str = "igredientes_picole"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_igrediente: int = sa.Column(sa.Integer, sa.ForeignKey("igredientes.id"))
    id_picole: int = sa.Column(sa.Integer, sa.ForeignKey("picoles.id"))

    def __str__(self) -> str:
        return f"<Igredientes: {self.id}>"

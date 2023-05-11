import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from .model_base import ModelBase
from .tipo_picole import TiposPicole


class Lotes(ModelBase):
    __tablename__: str = "lotes"
    __allow_unmapped__ = True

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picoles.id"))
    tipo_picole: TiposPicole = orm.relationship("TiposPicole", lazy='joined')  # orm faz mapeamento do objeto relacional
    quantidade: int = sa.Column(sa.Integer, default=0)

    def __str__(self) -> str:
        return f"<Lotes: {self.nome}>"

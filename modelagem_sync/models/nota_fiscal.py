from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from .model_base import ModelBase
from .revendedor import Revendedores
from .lote import Lotes


# notas fiscais podem ter vários lotes
lotes_nota_fiscal = sa.Table(
    "lotes_notas_fiscal",
    ModelBase.metadata,
    sa.Column("id_notas_fiscais", sa.Integer, sa.ForeignKey("notas_fiscais.id")),
    sa.Column("id_lote", sa.Integer, sa.ForeignKey("lotes.id"))
)


class NotasFiscais(ModelBase):
    __tablename__: str = "notas_fiscais"
    __allow_unmapped__ = True

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    numero_serie: str = sa.Column(sa.String(45), nullable=False, unique=True)
    valor: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    data: datetime = sa.Column(sa.DateTime, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False, unique=True)
    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey("revendedores.id"))
    revendedor: Revendedores = orm.Relationship("Revendedores", lazy="joined")

    # uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lotes] = orm.Relationship('Lotes', secondary=lotes_nota_fiscal, lazy="dynamic",
                                          backref="lotes")

    def __str__(self) -> str:
        return f"<NotasFiscais: {self.numero_serie}>"

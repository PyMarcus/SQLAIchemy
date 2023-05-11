import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from model_base import ModelBase
from lote import Lotes
from nota_fiscal import NotasFiscais


class LotesNotasFiscais(ModelBase):
    __tablename__: str = "lotes_notas_fiscais"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey("lotes.id"))
    id_nota_fiscal: int = sa.Column(sa.Integer, sa.ForeignKey("notas_fiscais.id"))
    notas_fiscais: NotasFiscais = orm.relationship("NotasFiscais", lazy="joined")

    def __str__(self) -> str:
        return f"<LotesNotasFiscais: {self.notas_fiscais}>"

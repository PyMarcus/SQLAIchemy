from typing import List, Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from .model_base import ModelBase
from .igrediente import Igredientes
from .sabor import Sabores
from .tipo_embalagem import TiposEmbalagens
from .conservante import Conservantes
from .aditivo_nutritivo import AditivoNutritivo


# picole pode ter varios igredientes
igredientes_picole = sa.Table(
    "igredientes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_igredientes", sa.Integer, sa.ForeignKey("igredientes.id"))
)


# picole pode ter varios conservantes
conservantes_picole = sa.Table(
    "conservantes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_conservante", sa.Integer, sa.ForeignKey("conservantes.id"))
)


# picole pode ter vários aditivos
aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_aditivos_nutritivos", sa.Integer, sa.ForeignKey("aditivos_nutritivos.id"))
)


class Picoles(ModelBase):
    __tablename__: str = "picoles"
    __allow_unmapped__ = True

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey("sabores.id"))
    sabor: Sabores = orm.relationship("Sabores", lazy="joined")
    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_embalagens.id"))
    tipo_embalagem: TiposEmbalagens = orm.relationship("TiposEmbalagens", lazy="joined")

    # um picole pode ter vários igredientes
    igredientes: List[Igredientes] = orm.relationship("Igredientes", secondary=igredientes_picole,
                                                  backref="igredientes_picole", lazy="joined")

    # um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[List[Conservantes]] = orm.relationship("Conservantes", secondary=conservantes_picole,
                                                  backref="conservantes", lazy="joined")
    # um picole pode ter vários aditivos nutrivos ou nenhum
    aditivo_nutritivo: Optional[List[AditivoNutritivo]] = orm.relationship("AditivoNutritivo", secondary=aditivos_nutritivos_picole,
                                                                  backref="aditivos_nutritivos", lazy="joined")

    def __str__(self) -> str:
        return f"<Picoles: {self.sabor}>"

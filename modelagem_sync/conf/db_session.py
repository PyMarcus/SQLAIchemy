import sqlalchemy as sa
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine | None:
    """
    Create engine instance (Conexão com o banco de dados)
    """
    global __engine

    if __engine:
        return

    if sqlite:
        file_db: str = "db/database.sqlite"
        folder: Path = Path(file_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        connection: str = f"sqlite:///{file_db}"
        __engine = sa.create_engine(url=connection,
                                    echo=False,
                                    connect_args={"check_same_thread": False})
    else:
        # postgresql
        connection: str = f"postgresql://sqlalchemy:sqlalchemy@localhost:5432/sqlalchemy"
        __engine = sa.create_engine(url=connection, echo=False)
    return __engine


def create_session() -> Session:
    """
    Create a new session with database
    :return: Session
    """
    global __engine

    if not __engine:
        create_engine()  # if sqlite = true

    __session: sessionmaker = sessionmaker(__engine, expire_on_commit=False, class_=Session)  # expire define if objects are expired from session
    session: Session = __session()
    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()
    from models import __all_models

    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)

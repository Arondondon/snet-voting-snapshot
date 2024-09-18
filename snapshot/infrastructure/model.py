from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UniqueConstraint
from sqlalchemy import text
from sqlalchemy.dialects.mysql import TIMESTAMP, VARCHAR, INTEGER, BIGINT, TEXT
from snapshot.config import DB_CONFIG, SNAPSHOT_TABLES


Base = declarative_base()

on_create = text("CURRENT_TIMESTAMP")
on_update = text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")


class Balances(Base):

    __tablename__ = SNAPSHOT_TABLES["BALANCES"]

    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    network = Column("network", VARCHAR(50), nullable=False)
    address = Column("address", VARCHAR(255), unique=True, nullable=False)
    stake_key = Column("stake_key", VARCHAR(255), nullable=True)
    balance = Column("balance", BIGINT, nullable=False, default=0)
    stake = Column("stake", BIGINT, nullable=False, default=0)
    created_on = Column("created_on", TIMESTAMP(timezone=False), nullable=False, server_default=on_create)
    updated_on = Column("updated_on", TIMESTAMP(timezone=False), nullable=False, server_default=on_update)



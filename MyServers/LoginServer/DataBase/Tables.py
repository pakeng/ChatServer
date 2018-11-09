from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

from MyServers.LoginServer.DBHelper.DateBaseHelper import DBHelper

dbHelper = DBHelper()
engine = dbHelper.get_db_engine()

Base = declarative_base()


# 创建单表
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    uid = Column(String(32))
    pwd = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', 'uid', name='uix_id_name_uid'),
       Index('ix_id_name_uid', 'uid', 'name'),
    )



Base.metadata.create_all(engine)  #创建表
# Base.metadata.drop_all(engine)   #删除表
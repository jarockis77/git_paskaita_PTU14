from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
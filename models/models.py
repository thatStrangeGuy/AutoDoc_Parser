# TODO: Handle models for working with database, maybe add pydantic for data validation
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class IndexType(Base):
    __tablename__ = 'index_types'

    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False, unique=True)
    dictionaries = relationship("Dictionary", order_by='Dictionary.ID', back_populates="index_type", cascade="all, delete-orphan")


class ValueType(Base):
    __tablename__ = 'value_types'

    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False, unique=True)
    dictionaries = relationship("Dictionary", order_by='Dictionary.ID', back_populates="value_type", cascade="all, delete-orphan")


class Dictionary(Base):
    __tablename__ = 'dictionaries'

    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False, unique=True)
    IndexTypeID = Column(Integer, ForeignKey('index_types.ID', ondelete="CASCADE"))
    index_type = relationship("IndexType", back_populates="dictionaries")
    index = Column(String, nullable=False)
    Column_Name = Column(String, nullable=False)
    Key = Column(String, nullable=False)
    ValueTypeID = Column(Integer, ForeignKey('value_types.ID', ondelete='CASCADE'))
    value_type = relationship("ValueType", back_populates="dictionaries")
    Value = Column(String, nullable=False)
    OrderID = Column(Integer, nullable=False, unique=True)

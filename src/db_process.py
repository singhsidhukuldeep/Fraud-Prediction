from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Numeric, Column, ForeignKey, Integer, String, Float


SQL_DB_URL = "sqlite:///./all_requests.db"

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})
_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class apiCalls(Base):
    __tablename__ = "apiCalls"

    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer)
    type = Column(String)
    amount = Column(Numeric(10, 2))
    nameOrig = Column(String)
    oldbalanceOrig = Column(Numeric(10, 2))
    newbalanceOrig = Column(Numeric(10, 2))
    nameDest = Column(String)
    oldbalanceDest = Column(Numeric(10, 2))
    newbalanceDest = Column(Numeric(10, 2))


Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = _session()
        yield db
    finally:
        db.close()

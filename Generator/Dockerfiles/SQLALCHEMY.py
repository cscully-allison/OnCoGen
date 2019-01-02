from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('postgresql://OnCoGen:OnCoGen@10.0.75.0:5432/NRDC_Database', echo=True)
Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'testtable'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

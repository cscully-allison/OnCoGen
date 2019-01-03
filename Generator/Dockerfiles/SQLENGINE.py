from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine('postgresql://OnCoGen:OnCoGen@127.0.0.1:5432/NRDC_Database', echo=True)
Base = declarative_base

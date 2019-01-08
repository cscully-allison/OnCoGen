'''
  This is an automatically generated file. Please do not edit it directly.

'''


from sqlalchemy import Column, Integer, String, Float, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine('postgresql://OnCoGen:OnCoGen@oncogen_db:5432/NRDC_DB', echo=True)
Base = declarative_base()

class Site_Network(Base):
    __tablename__ = 'Site_Network'

    Alias = Column('Alias', String)
    Grant_Number_String = Column('Grant Number String', String)
    Started_Date = Column('Started Date', DateTime)
    Network = Column('Network', Integer, primary_key=True)
    Unique_Identifier = Column('Unique Identifier', String)
    Name = Column('Name', String)
    Original_Funding_Agency = Column('Original Funding Agency', String)
    Institution_Name = Column('Institution Name', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Component(Base):
    __tablename__ = 'Component'

    Last_Calibrated_Date = Column('Last Calibrated Date', DateTime)
    Creation_Date = Column('Creation Date', DateTime)
    Vendor = Column('Vendor', String)
    Name = Column('Name', String)
    Manufacturer = Column('Manufacturer', String)
    Unique_Identifier = Column('Unique Identifier', String)
    Serial_Number = Column('Serial Number', String)
    Supplier = Column('Supplier', String)
    Modification_Date = Column('Modification Date', DateTime)
    Component = Column('Component', Integer, primary_key=True)
    Photo = Column('Photo', LargeBinary)
    Model = Column('Model', String)
    Installation_Date = Column('Installation Date', DateTime)
    Installation_Details = Column('Installation Details', String)
    Wiring_Notes = Column('Wiring Notes', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class System(Base):
    __tablename__ = 'System'

    Modification_Date = Column('Modification Date', DateTime)
    Creation_Date = Column('Creation Date', DateTime)
    System = Column('System', Integer, primary_key=True)
    Power = Column('Power', String)
    Installation_Location = Column('Installation Location', String)
    Photo = Column('Photo', LargeBinary)
    Unique_Identifier = Column('Unique Identifier', String)
    Name = Column('Name', String)
    Details = Column('Details', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Deployment(Base):
    __tablename__ = 'Deployment'

    Abandoned_Date = Column('Abandoned Date', DateTime)
    Notes = Column('Notes', String)
    Deployment = Column('Deployment', Integer, primary_key=True)
    Creation_Date = Column('Creation Date', DateTime)
    Parent_Logger = Column('Parent Logger', String)
    Height_From_Ground = Column('Height From Ground', Float)
    Modification_Date = Column('Modification Date', DateTime)
    Unique_Identifier = Column('Unique Identifier', String)
    Established_Date = Column('Established Date', DateTime)
    Purpose = Column('Purpose', String)
    Name = Column('Name', String)
    Center_Offset = Column('Center Offset', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Site(Base):
    __tablename__ = 'Site'

    Unique_Identifier = Column('Unique Identifier', String)
    Landmark_Photo = Column('Landmark Photo', LargeBinary)
    Site = Column('Site', Integer, primary_key=True)
    Alias = Column('Alias', String)
    Name = Column('Name', String)
    Time_Zone_Offset = Column('Time Zone Offset', Integer)
    Notes = Column('Notes', String)
    Time_Zone_Abbreviation = Column('Time Zone Abbreviation', String)
    Time_Zone_Name = Column('Time Zone Name', String)
    GPS_Landmark = Column('GPS Landmark', String)
    Creation_Date = Column('Creation Date', DateTime)
    Modification_Date = Column('Modification Date', DateTime)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)




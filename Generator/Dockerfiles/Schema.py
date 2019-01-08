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

    Institution_Name = Column('Institution Name', String)
    Network = Column('Network', Integer, primary_key=True)
    Unique_Identifier = Column('Unique Identifier', String)
    Grant_Number_String = Column('Grant Number String', String)
    Alias = Column('Alias', String)
    Name = Column('Name', String)
    Started_Date = Column('Started Date', DateTime)
    Original_Funding_Agency = Column('Original Funding Agency', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class System(Base):
    __tablename__ = 'System'

    Unique_Identifier = Column('Unique Identifier', String)
    Creation_Date = Column('Creation Date', DateTime)
    Installation_Location = Column('Installation Location', String)
    Photo = Column('Photo', LargeBinary)
    Power = Column('Power', String)
    System = Column('System', Integer, primary_key=True)
    Modification_Date = Column('Modification Date', DateTime)
    Details = Column('Details', String)
    Name = Column('Name', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Site(Base):
    __tablename__ = 'Site'

    GPS_Landmark = Column('GPS Landmark', String)
    Site = Column('Site', Integer, primary_key=True)
    Unique_Identifier = Column('Unique Identifier', String)
    Name = Column('Name', String)
    Modification_Date = Column('Modification Date', DateTime)
    Alias = Column('Alias', String)
    Time_Zone_Offset = Column('Time Zone Offset', Integer)
    Time_Zone_Name = Column('Time Zone Name', String)
    Landmark_Photo = Column('Landmark Photo', LargeBinary)
    Notes = Column('Notes', String)
    Creation_Date = Column('Creation Date', DateTime)
    Time_Zone_Abbreviation = Column('Time Zone Abbreviation', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Component(Base):
    __tablename__ = 'Component'

    Serial_Number = Column('Serial Number', String)
    Component = Column('Component', Integer, primary_key=True)
    Manufacturer = Column('Manufacturer', String)
    Installation_Date = Column('Installation Date', DateTime)
    Modification_Date = Column('Modification Date', DateTime)
    Model = Column('Model', String)
    Photo = Column('Photo', LargeBinary)
    Supplier = Column('Supplier', String)
    Creation_Date = Column('Creation Date', DateTime)
    Vendor = Column('Vendor', String)
    Name = Column('Name', String)
    Installation_Details = Column('Installation Details', String)
    Last_Calibrated_Date = Column('Last Calibrated Date', DateTime)
    Unique_Identifier = Column('Unique Identifier', String)
    Wiring_Notes = Column('Wiring Notes', String)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Deployment(Base):
    __tablename__ = 'Deployment'

    Modification_Date = Column('Modification Date', DateTime)
    Parent_Logger = Column('Parent Logger', String)
    Notes = Column('Notes', String)
    Established_Date = Column('Established Date', DateTime)
    Creation_Date = Column('Creation Date', DateTime)
    Center_Offset = Column('Center Offset', String)
    Name = Column('Name', String)
    Abandoned_Date = Column('Abandoned Date', DateTime)
    Height_From_Ground = Column('Height From Ground', Float)
    Unique_Identifier = Column('Unique Identifier', String)
    Purpose = Column('Purpose', String)
    Deployment = Column('Deployment', Integer, primary_key=True)
    
    

  #  def __repr__(self):
  #      return "<testtable(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)




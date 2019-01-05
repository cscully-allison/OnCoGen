from abc import ABCMeta, abstractmethod
from Utilities import GetConfiguration, UnderscoreSpaces
from rdflib import URIRef
import json


class DBInitializerInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def DefineSchemaAsClass(self, Schema):
        pass

    @abstractmethod
    def CreateSchemas(self):
        pass

class DBInitializer(DBInitializerInterface):
    def __init__(self, Configuration):
        self.Configuration = Configuration['main']
        with open(Configuration['lexicon'], 'r') as JsonData:
            self.Lexicon = json.load(JsonData)
        self.Templates = 'Templates/PythonTemplates/'
        self.SchemaFile = ''
        self.SchemaClass = ''
        self.ColumnDefinition = ''
        self.ConnStr = GetConfiguration(self.Configuration, 'ConnectionString', None)
        self.FetchTemplates()

    def ManageDatatype(self, DT):
        DTStr = ''
        if ':' in DT:
            DTStr = DT.split(':')[-1]
        elif '#' in DT:
            DTStr = DT.split('#')[-1]
        else:
            DTStr = string(DT)
        return self.Lexicon['datatypes'][DTStr]

    def FetchTemplates(self):
        file = GetConfiguration(self.Configuration, 'ColumnTemplate', None)
        file = self.Templates + file
        with open(file, 'r') as f:
            self.ColumnDefintion = f.read()

        file = GetConfiguration(self.Configuration, 'SAClassTemplate', None)
        file = self.Templates + file
        with open(file, 'r') as f:
            self.SchemaClass = f.read()

        file = GetConfiguration(self.Configuration, 'SAFileTemplate', None)
        file = self.Templates + file
        with open(file, 'r') as f:
            self.SchemaFile = f.read()

    def FormatColumn(self, Characteristic):
        VarLabel = UnderscoreSpaces(Characteristic['Label'])
        StrictLabel = Characteristic['Label']
        DataType = self.ManageDatatype(Characteristic['Datatype'])

        Column = self.ColumnDefintion.format(VarLabel, "'"+StrictLabel+"'", DataType, '{}')

        if Characteristic['PrimaryKey'] is True:
            PrimaryKey = ", primary_key=True{}"
            Column = Column.format(PrimaryKey)
            pass
        if Characteristic['Autoincrement'] is True:
            pass
        elif Characteristic['ForeignKey'] is True:
            pass

        Column = Column.format('')
        Column = Column.replace('\n', '')

        return Column

    def DefineSchemaAsClass(self, ClassLabel, Schema):
        ClassTemplate = self.SchemaClass
        ClassLabelUnderscore = UnderscoreSpaces(ClassLabel)

        ClassTemplate = ClassTemplate.format(ClassLabelUnderscore, '{}\n'.rjust(7) + '{}'.rjust(6))
        for Characteristic in Schema['Characteristics']:
            Column = self.FormatColumn(Characteristic)
            ClassTemplate = ClassTemplate.format(Column, '{}\n' + '{}'.rjust(6))

        ClassTemplate = ClassTemplate.format('','')

        return ClassTemplate

    def CreateSchemas(self, SchemaBundle, DBName):
        ClassDef = ''
        ConnectionString = self.ConnStr.format(DBName)


        for Tier in SchemaBundle:
            ClassDef += self.DefineSchemaAsClass(Tier, SchemaBundle[Tier]) + '\n\n'

        SchemaFile = self.SchemaFile.format(ConnectionString, ClassDef)
        print SchemaFile
        return SchemaFile

    def OutputSchemaFile(self, file):
        pass

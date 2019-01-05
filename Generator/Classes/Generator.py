from Parser import Parser
from Containerizer import Containerizer
from DBManager import DBInitializer

class Generator():

    def __init__(self, Configuration, OntologySrc):
        self.Parser = Parser(Configuration, OntologySrc)
        self.ContBuilder = Containerizer(Configuration)
        self.DBI = DBInitializer(Configuration)
        self.BuildContainers()

    def BuildContainers(self):
        ServiceCount = self.Parser.GetServiceCounts()
        DBName = self.Parser.GetDatabaseName()
        Schema = self.Parser.GetHierarchicalSchemaData()
        self.ContBuilder.BuildComposeTemplate(DBName, {})
        self.DBI.CreateSchemas(Schema, DBName)
        self.ContBuilder.OutputFinalYAML()



    def BuildTable():
        pass

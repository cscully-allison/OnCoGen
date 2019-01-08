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
        #Parse and get metadata from Ontology
        ServiceCount = self.Parser.GetServiceCounts()
        DBName = self.Parser.GetDatabaseName()
        Schema = self.Parser.GetHierarchicalSchemaData()

        self.DBI.CreateSchemas(Schema, DBName)
        self.DBI.OutputSchemaFile()
        BuildTableFile = self.DBI.BuildTablesUsingSchema()

        #Begin building container
        self.ContBuilder.BuildComposeTemplate(DBName, Schema, BuildTableFile)

        self.ContBuilder.OutputFinalYAML()



    def BuildTable():
        pass

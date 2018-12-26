from Parser import Parser
from Containerizer import Containerizer

class Generator():

    def __init__(self, Configuration, OntologySrc):
        self.Parser = Parser(Configuration, OntologySrc)
        self.ContBuilder = Containerizer(Configuration)
        self.BuildContainers()

    def BuildContainers(self):
        ServiceCount = self.Parser.GetServiceCounts()
        DBName = self.Parser.GetDatabaseName()
        self.ContBuilder.BuildComposeTemplate(DBName, {})
        self.ContBuilder.OutputFinalYAML()



    def BuildTable():
        pass

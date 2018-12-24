import xml.etree.ElementTree as ET

class Containerizer():
    def __init__(self, Configuration):
        self.Configuration = Configuration #configuration file
        self.ElementsFolder = 'ComposeElements/'
        self.SQLFolder = 'SQL_Templates/'
        self.ComposeTemplate = ''
        self.DBComposeSubTemplate = ''
        self.SQLInit = ''
        self.WebServiceSubTemplate = ''
        self.FinalYAML = ''

        Tree = ET.parse(Configuration)
        Root = Tree.getroot()

        CompElem = self.GetNodeFromConf(Root, 'ComposeElements')
        self.GetElementsTemplates(CompElem)

        SQLConf = self.GetNodeFromConf(Root, 'SQL')
        self.GetSQLTemplates(SQLConf)

    def GetSQLTemplates(self, SQLConf):
        templatefile = ''
        for Child in SQLConf:
            if Child.tag == 'InitTemplate':
                templatefile = Child.text
                templatefile = self.SQLFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.SQLInit = F.read()

    def GetNodeFromConf(self, Root, SubRoot):
        for Child in Root:
            if Child.tag == SubRoot:
                CompElem = Child

        return CompElem

    def GetElementsTemplates(self, CE):
        templatefile = ''
        for Child in CE:
            if Child.tag == 'DB':
                templatefile = Child.text
                templatefile = self.ElementsFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.DBComposeSubTemplate = F.read()
            elif Child.tag == 'Services':
                templatefile = Child.text
                templatefile = self.ElementsFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.WebServiceSubTemplate = F.read()
            elif Child.tag == 'BaseTemplate':
                templatefile = Child.text
                templatefile = self.ElementsFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.ComposeTemplate = F.read()
        return

    def BuildWebServices(self, ServiceInfo):
        return ''

    def BuildDatabase(self, DBName):
        DBTemplate = ''
        InitTemplate = ''
        Password = 'OnCoGen'
        User = 'OnCoGen'

        #build database template
        DBTemplate = self.DBComposeSubTemplate.format('db')
        InitTemplate = self.SQLInit.format(DBName, User, Password)

        with open('SQL/init.sql', 'w') as Fout:
            Fout.write(InitTemplate)

        return DBTemplate

    def BuildComposeTemplate(self, DBName, ServiceInfo):
        DBTemplate = self.BuildDatabase(DBName)
        WebServices = self.BuildWebServices(ServiceInfo)

        self.FinalYAML = self.ComposeTemplate.format(DBTemplate, WebServices)

    def OutputFinalYAML(self):
        with open('docker-compose.yml', 'w') as Fout:
            Fout.write(self.FinalYAML)

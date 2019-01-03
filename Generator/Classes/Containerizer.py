import xml.etree.ElementTree as ET

class Containerizer():
    def __init__(self, Configuration):
        self.Configuration = Configuration #configuration file
        self.ElementsFolder = 'Templates/ComposeElements/'
        self.DockerTemplateFolder= 'Templates/DockerfileTemplates/'
        self.ComposeTemplate = ''
        self.DBComposeSubTemplate = ''
        self.WebServiceSubTemplate = ''
        self.FinalYAML = ''
        self.DBDFTemplate = ''
        self.DBServTemplate = ''


        Tree = ET.parse(Configuration)
        Root = Tree.getroot()

        CompElem = self.GetNodeFromConf(Root, 'ComposeElements')
        self.GetElementsTemplates(CompElem)

        DockerConf = self.GetNodeFromConf(Root, 'Dockerfile')
        self.GetDockerTemplates(DockerConf)

        print(self.DBDFTemplate)
        print(self.DBServTemplate)

    def GetDockerTemplates(self, Dockerconf):
        templatefile = ''
        for Child in Dockerconf:
            if Child.tag == 'DBDockerfile':
                templatefile = Child.text
                templatefile = self.DockerTemplateFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.DBDFTemplate = F.read()
            if Child.tag == 'ServiceDockerfile':
                templatefile = Child.text
                templatefile = self.DockerTemplateFolder + templatefile
                with open(templatefile, 'r') as F:
                    self.DBServTemplate = F.read()

    def GetNodeFromConf(self, Root, SubRoot):
        for Child in Root:
            if Child.tag == SubRoot:
                CompElem = Child

        return CompElem

    def GetElementsTemplates(self, CE):
        templatefile = ''
        for C in CE:
            if C.tag == 'DB':
                for Child in C:
                    if Child.tag == 'ElementName':
                        templatefile = Child.text
                        templatefile = self.ElementsFolder + templatefile
                        with open(templatefile, 'r') as F:
                            self.DBComposeSubTemplate = F.read()
            elif C.tag == 'Services':
                for Child in C:
                    if Child.tag == 'ElementName':
                        templatefile = Child.text
                        templatefile = self.ElementsFolder + templatefile
                        with open(templatefile, 'r') as F:
                            self.WebServiceSubTemplate = F.read()
            elif C.tag == 'BaseTemplate':
                for Child in C:
                    if Child.tag == 'ElementName':
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
        DBTemplate = self.DBComposeSubTemplate.format('oncogen_db')
        FormattedDBDFT = self.DBDFTemplate.format(User, Password, DBName)

        with open('Dockerfiles/DBDockerfile', 'w') as Fout:
            Fout.write(FormattedDBDFT)

        return DBTemplate


    def BuildComposeTemplate(self, DBName, ServiceInfo):
        DBTemplate = self.BuildDatabase(DBName)
        WebServices = self.BuildWebServices(ServiceInfo)

        self.FinalYAML = self.ComposeTemplate.format(DBTemplate, WebServices)

    def OutputFinalYAML(self):
        with open('docker-compose.yml', 'w') as Fout:
            Fout.write(self.FinalYAML)

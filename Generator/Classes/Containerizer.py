import xml.etree.ElementTree as ET

class Containerizer():
    def __init__(Configuration):
        self.Configuration = Configuration #configuration file
        self.ElementsFolder = 'ComposeElements/'
        self.ComposeTemplate = ''
        self.DBComposeSubTemplate = ''
        self.WebServiceSubTemplate = ''

        Tree = ET.parse(Configuration)
        Root = Tree.getroot()

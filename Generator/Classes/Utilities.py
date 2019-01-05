
import xml.etree.ElementTree as ET

def GetConfiguration(ConfigFile, Tag, Root):
    Config = ''

    if Root is None:
        Tree = ET.parse(ConfigFile)
        Root = Tree.getroot()

    if type(Root) is type(''):
        Config = ''
    elif Root.tag == Tag:
        Config = Root.text
    else:
        for Child in Root:
            Temp = GetConfiguration(ConfigFile, Tag, Child)
            if Temp is not '':
                Config = Temp


    return Config


def UnderscoreSpaces(text):
    return text.replace(' ', '_')

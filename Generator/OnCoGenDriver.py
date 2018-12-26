import sys
sys.path.insert(0, './Classes/')
from Generator import Generator



def Main():
    OnCoGen = Generator('Configurations/configuration.xml', 'Ontology/NRDCOntology.xml')


Main()

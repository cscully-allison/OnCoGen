import sys
sys.path.insert(0, './Classes/')
from Generator import Generator



def Main():
    ConfigurationBundle = {'main':'Configurations/configuration.xml', 'lexicon':'Configurations/word_mappings.json'}
    OnCoGen = Generator(ConfigurationBundle, 'Ontology/NRDCOntology.xml')


Main()

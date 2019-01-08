import sys
sys.path.insert(0, './Classes/')
from Generator import Generator



def Main():
    print("Generating")
    OntologyFile = 'Ontology/NRDCOntology.xml'
    ConfigurationBundle = {'main':'Configurations/configuration.xml', 'lexicon':'Configurations/word_mappings.json'}

    for i, arg in enumerate(sys.argv):
        if arg == "-i":
            OntologyFile = sys.argv[i+1]

    OnCoGen = Generator(ConfigurationBundle, OntologyFile)
    print(". . . Done")

Main()

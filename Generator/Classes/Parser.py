from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, DC, OWL
import xml.etree.ElementTree as ET

class Parser():

    def __init__(self, Configuration, OwlSrc=""):
        self.OwlSrc = OwlSrc
        self.Graph = Graph()
        self.TripleStore = []
        self.Namespace = Namespace(self.GetConfiguration(Configuration, 'Namespace'))
        self.LayerTerminology = self.GetConfiguration(Configuration, 'LayerTerminology')


    def GetOwlSrc(self):
        return self.OwlSrc

    def GetConfiguration(self, ConfigFile, Tag):
        OntConf = None
        Tree = ET.parse(ConfigFile)
        Root = Tree.getroot()

        for Child in Root:
            if Child.tag == "Ontology":
                OntConf = Child

        for Child in OntConf:
            if Child.tag == Tag:
                return Child.text

    #combines a text refrent with our namespace
    def BuildURIRef(self, Namespace, Referent):
        return URIRef(Namespace + '#' + Referent)

    def GetDatabaseName(self):
        self.Graph.parse(self.OwlSrc)
        NS = URIRef(self.Namespace)
        Abbreviation = self.BuildURIRef(self.Namespace, 'abbreviation')

        for s,p,o in self.Graph.triples((NS, Abbreviation, None)):
            Name = o.replace(' ', '_')
            return Name + "_DB"


    #retrieves a count for the number of services we will Requires
    #todo: check for associated entities
    def GetServiceCounts(self):
        self.Graph.parse(self.OwlSrc)

        count = 0
        LayerDescriptor = self.BuildURIRef(self.Namespace, self.LayerTerminology)

        for s,p,o in self.Graph.triples((None, RDF.type, LayerDescriptor)):
            count += 1

        return count



    def query(self):

        S = URIRef("http://www.sensor.nevada.edu/ontologies/research_site_hierarchy#site")
        SN = URIRef("http://www.sensor.nevada.edu/ontologies/research_site_hierarchy#site-network")
        OT = URIRef("http://www.sensor.nevada.edu/ontologies/research_site_hierarchy#organizational_tier")

        NRDC_RSH = Namespace("https://www.sensor.nevada.edu/ontologies/research_site_hierarchy#")




        # import pprint
        # for tier in list(self.Graph[:RDF.type:OT]):
        #     print(tier)
        #     pprint.pprint(list(self.Graph[tier]))


        for s,p,o in self.Graph.triples((S, NRDC_RSH.characteristic, None)):
            print("%s is a charactertistic of site"%(o))
            for su,pr,ob in self.Graph.triples((o, None, None)):
                print("%s is the %s of %s"%(ob,pr,su))

        # for s, p, o in g.triples((None, NRDC_RSH.parentOf, None)):
        #     print("%s is parent of %s"%(s, o))
        #     for su,pr,ob in g.triples((s, NRDC_RSH.characteristic, None)):
        #         print("The parent of " + o + " is " + s +" and has the characteristic " + ob)
        #     for su, pr, ob in g.triples((s, NRDC_RSH.ordinalCharacteristic, None)):
        #         print(ob)

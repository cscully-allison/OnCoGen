from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, RDFS

class Parser():

    def __init__(self, OwlSrc=""):
        self.OwlSrc = OwlSrc
        self.Graph = Graph()
        self.TripleStore = []

    def GetOwlSrc(self):
        return self.OwlSrc

    def ReadInOntology(self):
        #query the ontology for specific key words
        #  - we need to make sure that the file format is correct
        #  - also need to make sure xml objects match ontology expectations



        #parse out triples (into groups of objects?)

        #return a list of triples

        return

    def query(self):


        self.Graph.parse(self.OwlSrc)


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

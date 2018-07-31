from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, RDFS

class Parser():

    def __init__(self, OwlSrc=""):
        self.OwlSrc = OwlSrc
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
        # queryString = "SELECT * WHERE { ?s ?p ?o. }"
        #
        # sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        # sparql.setQuery("""
        #     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        #     SELECT ?name
        #     WHERE {  ?s dbo:isPartOf <http://dbpedia.org/resource/Asturias>.
        #              ?s foaf:name ?name. }
        # """)
        # sparql.setReturnFormat(JSON)
        # results = sparql.query().convert()
        #
        # for result in results["results"]["bindings"]:
        #     print(u"{} is part of Asturias".format(result['name']["value"]))

        g = Graph()
        g.parse(self.OwlSrc)

        print(len(g))

        import pprint
        for trpl in g:
            pprint.pprint (trpl)

        SN = URIRef("http://www.sensor.nevada.edu/ontologies/research_site_hierarchy#site-network")
        OT = URIRef("http://www.sensor.nevada.edu/ontologies/research_site_hierarchy#organizational_tier")

        NRDC_RSH = Namespace("https://www.sensor.nevada.edu/ontologies/research_site_hierarchy#")

        # if(SN, RDF.type, OT) in g:
        #     print("This graph knows that Site Network is an orginizational tier!")

        for s, p, o in g.triples((None, NRDC_RSH.characteristic, None)):
            print("%s is characterized by %s"%(s, o))

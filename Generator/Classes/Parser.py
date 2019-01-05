from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, DC, OWL
import xml.etree.ElementTree as ET
import json
import pprint

pp = pprint.PrettyPrinter()

class Parser():

    def __init__(self, Configuration, OwlSrc=""):
        self.OwlSrc = OwlSrc
        self.Graph = Graph()
        self.TripleStore = []
        self.Namespace = Namespace(self.GetConfiguration(Configuration['main'], 'Namespace'))
        self.LayerTerminology = self.GetConfiguration(Configuration['main'], 'LayerTerminology')
        with open(Configuration['lexicon'], 'r') as JsonData:
            self.lexicon = json.load(JsonData)


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

        for s,p,o in self.Graph.triples((None, RDFS.subClassOf, LayerDescriptor)):
            count += 1

        return count

    def GetSingleCharacteristic(self, CharacteristicID):
        Characteristic = {"Datatype":'', "Label":'', "PrimaryKey": False, "ForeignKey": False, "Autoincrement": False}
        for s, p, o in self.Graph.triples((CharacteristicID, None, None)):
            if p == RDFS.label:
                Characteristic["Label"] = o
            if p == self.BuildURIRef(self.Namespace, "datatype"):
                Characteristic['Datatype'] = o

        return Characteristic

    def GetSingleSchema(self, SchemaName):
        Schema = []

        for s,p,o in self.Graph.triples((SchemaName, None, None)):
            if p.split('#')[-1] in self.lexicon["column-aliases"]["column"]:
                Characteristic = self.GetSingleCharacteristic(o)
                if Characteristic not in Schema:
                    Schema.append(Characteristic)

            elif p.split('#')[-1] in self.lexicon["column-aliases"]["primary-key"]:
                Characteristic = self.GetSingleCharacteristic(o)
                Characteristic["PrimaryKey"] = True
                Characteristic["Autoincrement"] = True
                if Characteristic not in Schema:
                    Schema.append(Characteristic)
            #foreign key goes here


        return Schema

    def GetHierarchicalSchemaData(self):
        SchemaBundle = {}
        self.Graph.parse(self.OwlSrc)
        LayerDescriptor = self.BuildURIRef(self.Namespace, self.LayerTerminology)

        for s,p,o in self.Graph.triples((None, RDFS.subClassOf, LayerDescriptor)):
            for su, pr, ob in self.Graph.triples((s, self.BuildURIRef(self.Namespace, "name"), None)):
                SchemaBundle[ob] = {"Characteristics":[], "Relations": {}, "Name": ob}
                SchemaBundle[ob]["Characteristics"] = self.GetSingleSchema(s)

        return SchemaBundle

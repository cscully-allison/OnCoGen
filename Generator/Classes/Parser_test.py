from Parser import Parser

#constructor test
def test_contructor():
    src = "../test.owl"
    tp = Parser(src)

    assert tp.OwlSrc == "../test.owl"

def test_query():
    src = "./Generator/Ontology/NRDCOntology.xml"
    tp = Parser(src)

    tp.query()


test_query()

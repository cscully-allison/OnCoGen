from Parser import Parser

#constructor test
def test_contructor():
    src = "file.owl"
    tp = Parser(src)

    assert tp.OwlSrc == src

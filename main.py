import sys

from errorManager import LexError, SynError, writeErrorFile
from lexAnalyzer import Lex, writeSuccessFile
from synAnalyzer import Syn
from node import generateXML, writeXML

def debug(tokens, xml):
    if 'lex' in sys.argv:
        print('--------TOKENS--------')
        for t in tokens:
            print(t)

    if 'syn' in sys.argv:
        print('--------TREE--------')
        print(xml)

try:
    lex = Lex(file_path='entrada.txt')
    tokens = lex.tokenize()

    syn = Syn(tokens)
    tree = syn.analyze()
    xml = generateXML(tree)

    if '-D' in sys.argv:
        debug(tokens, xml)
except (LexError, SynError) as e:
    print(e)
    writeErrorFile()
else:
    writeSuccessFile()
    writeXML(xml)

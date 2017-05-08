import sys

from errorManager import LexError, SynError, writeErrorFile
from lexAnalyzer import Lex, writeSuccessFile
from synAnalyzer import Syn
from node import generate_xml, check_semantic, write_xml

def debug(tokens, xml, symbols):
    if 'lex' in sys.argv:
        print('--------TOKENS--------')
        for t in tokens:
            print(t)

    if 'syn' in sys.argv:
        print('--------TREE--------')
        print(xml)

    if 'sem' in sys.argv:
        print('--------SYMBOLS--------')
        for key, value in symbols.items():
            print(value)

try:
    lex = Lex(file_path='entrada.txt')
    tokens = lex.tokenize()

    syn = Syn(tokens)
    tree = syn.analyze()
    xml = generate_xml(tree)
    check_semantic(tree)

    if '-D' in sys.argv:
        debug(tokens, xml, tree.sym_table)
except (LexError, SynError) as e:
    print(e)
    writeErrorFile()
else:
    writeSuccessFile()
    write_xml(xml)

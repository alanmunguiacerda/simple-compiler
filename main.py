import sys

from errorManager import LexError, SynError, SemError, writeErrorFile
from lexAnalyzer import Lex, writeSuccessFile
from synAnalyzer import Syn
from node import (
    generate_xml,
    check_semantic,
    write_xml,
    generate_code,
    write_code,
)


def debug(tokens, xml, symbols, code):
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

    if 'cod' in sys.argv:
        print('--------CODE--------')
        print(code)


try:
    lex = Lex(file_path='entrada.txt')
    tokens = lex.tokenize()

    syn = Syn(tokens)
    tree = syn.analyze()
    xml = generate_xml(tree)
    check_semantic(tree)
    code = generate_code(tree)

    if '-D' in sys.argv:
        debug(tokens, xml, tree.sym_table, code)
except (LexError, SynError, SemError) as e:
    print(e)
    writeErrorFile()
else:
    writeSuccessFile()
    write_xml(xml)
    write_code(code)

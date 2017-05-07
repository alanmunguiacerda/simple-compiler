import sys

from errorManager import LexError, SynError, writeErrorFile
from lexAnalyzer import Lex, writeSuccessFile
from synAnalyzer import Syn

def debug(tokens, tree):
    if 'lex' in sys.argv:
        print('--------TOKENS--------')
        for t in tokens:
            print(t)

    if 'syn' in sys.argv:
        print('--------TREE--------')
        json = tree.toJson()
        print(json)
        file = open('tree', 'w')
        file.write(json)
        file.close()

try:
    lex = Lex(file_path='entrada.txt')
    tokens = lex.tokenize()

    syn = Syn(tokens)
    tree = syn.analyze()

    if '-D' in sys.argv:
        debug(tokens, tree)
except (LexError, SynError) as e:
    print(e)
    writeErrorFile()
else:
    writeSuccessFile()

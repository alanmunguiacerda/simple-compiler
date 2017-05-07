import sys

from lexAnalyzer import Lex, writeSuccessFile
from errorManager import LexError, writeErrorFile

lex = Lex(file_path='entrada.txt')
try:
    lex.tokenize()
    if '-D' in sys.argv:
        print(tok)
except LexError as e:
    print(e)
    writeErrorFile()
else:
    writeSuccessFile()

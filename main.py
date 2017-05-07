from lexAnalyzer import Lex
from errorManager import LexError, writeErrorFile

lex = Lex(file_path='entrada.txt')

try:
    lex.tokenize()
    print(lex.tokens)
except LexError as e:
    print(e)
    writeErrorFile()

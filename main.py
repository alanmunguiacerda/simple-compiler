from lexAnalyzer import Lex, writeSuccessFile
from errorManager import LexError, writeErrorFile

lex = Lex(file_path='entrada.txt')

try:
    lex.tokenize()
    for tok in lex.tokens:
        print(tok)
except LexError as e:
    writeErrorFile()
else:
    writeSuccessFile()

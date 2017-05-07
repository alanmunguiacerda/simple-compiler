from lexAnalyzer import Lex, writeSuccessFile
from errorManager import LexError, writeErrorFile

lex = Lex(file_path='entrada.txt')

try:
    lex.tokenize()
except LexError as e:
    writeErrorFile()
else:
    writeSuccessFile()

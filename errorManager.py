class LexError(Exception):
    pass

def writeErrorFile():
    file = open('salida.txt', 'w')
    file.write('0')
    file.close()

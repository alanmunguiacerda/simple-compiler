class LexError(Exception):
    def __init__(self, message):

def writeErrorFile():
    file = open('salida.txt', 'w')
    file.write('1')
    file.close()

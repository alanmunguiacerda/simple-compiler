class LexError(Exception):
    pass


class SynError(Exception):
    pass


class SemError(Exception):
    pass


def writeErrorFile():
    file = open('salida.txt', 'w')
    file.write('0')
    file.close()

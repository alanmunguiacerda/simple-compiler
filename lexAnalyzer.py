from errorManager import LexError
from tokenPatterns import TOKEN_PATTERN, NEWLN, SPACE, RES_WORD, OP_LOG, RES_WORDS, OPS_LOG, END_TOKEN

IGNORED_TOKENS = frozenset([NEWLN, SPACE])

class Lex:
    def __init__(self, file_path):
        self.set_file(file_path)
        self.tokens = []

    def set_file(self, file_path):
        file = open(file_path)
        self.string = file.read()
        self.string += END_TOKEN

    def tokenize(self):
        pos = 0

        while True:
            m = TOKEN_PATTERN.match(self.string, pos)
            if not m:
                if pos == len(self.string) - 1:
                    self.tokens.append((END_TOKEN, END_TOKEN))
                    return self.tokens
                invalid = self.string[pos]
                raise LexError('Invalid token {0}'.format(invalid))

            token_name = m.lastgroup

            pos = m.end()

            token_value = m.group(token_name)
            if token_value in RES_WORDS:
                token_name = RES_WORD
            elif token_value in OPS_LOG:
                token_name = OP_LOG

            if token_name not in IGNORED_TOKENS:
                self.tokens.append((token_name, token_value))

def writeSuccessFile():
    file = open('salida.txt', 'w')
    file.write('1')
    file.close()

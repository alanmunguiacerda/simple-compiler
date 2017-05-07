from ErrorManager import ErrorManager
from tokenPatterns import TOKEN_PATTERN, NEWLN, SPACE, BLOCK_COM, LINE_COM

END_TOKEN = '$'

class LexicalAnalyzer:
    def __init__(self, file_path):
        self.set_file(file_path)
        self.global_pos = 0
        self.col = 0
        self.start_row = 0
        self.row = 1
        self.tokens = []

    def set_file(self, file_path):
        file = open(file_path)
        self.string = ''.join(file.readlines())
        self.string += END_TOKEN

    def next(self):
        while True:
            m = TOKEN_PATTERN.match(self.string, self.global_pos)
            if not m:
                if self.global_pos == len(self.string) - 1:
                    self.tokens.append(('', END_TOKEN))
                    return ('', END_TOKEN)
                if self.global_pos >= len(self.string) or ErrorManager.errorCount >= MAX_ERRORS:
                    self.tokens.append(None)
                    return self.current()
                self.global_pos += 1
                self.col = self.global_pos - self.start_row
                ErrorManager.lexicalError(self.row, self.col, 'Invalid token {0}'.format(self.string[self.global_pos-1]))
                continue

            token_name = m.lastgroup

            self.global_pos = m.end()

            if token_name in [NEWLN, LINE_COM]:
                self.row += 1
                self.start_row = self.global_pos
            elif token_name == BLOCK_COM:
                token_value = m.group(token_name)
                lines = token_value.count('\n')
                self.row += lines
                self.start_row = self.global_pos
            elif token_name != SPACE:
                token_value = m.group(token_name)
                self.tokens.append((token_name, token_value))
                return self.current()

    def current(self):
        return self.tokens[-1]

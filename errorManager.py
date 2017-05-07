class ErrorManager:
    errorCount = 0

    def lexicalError(row, col, message):
        print('[{0}, {1}] [lex] {2}'.format(row, col, message))
        ErrorManager.errorCount += 1

    def syntacticError(row, col, message):
        print('[{0}, {1}] [syn] {2}'.format(row, col, message))
        ErrorManager.errorCount += 1

    def semanticError(row, col, message):
        print('[{0}, {1}] [sem] {2}'.format(row, col, message))
        ErrorManager.errorCount += 1

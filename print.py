from node import Node
from dataTypes import D_TYPES
from errorManager import SemError


class Print(Node):
    def __init__(self, expr):
        super(Print, self).__init__()
        self.expr = expr

    def generate_xml(self):
        xml = '<IMPRIME><EXPRESION>'
        xml += self.expr.generate_xml()
        xml += '</EXPRESION></IMPRIME>'
        return xml

    def semantic(self):
        self.expr.semantic()

        if self.expr.type == D_TYPES['error']:
            raise SemError('Invalid print expression')
            return

        self.type = D_TYPES['void']

    def generate_code(self):
        expr = self.expr.generate_code()

        print_code = [
            'pop rax',
            'mov rdi, fmt',
            'mov rsi, rax',
            'call printf',
        ]

        return expr + print_code

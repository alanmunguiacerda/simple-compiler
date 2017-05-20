from node import Node
from dataTypes import D_TYPES
from errorManager import SemError


class UnaryExpression(Node):
    def __init__(self, op, expr):
        super(UnaryExpression, self).__init__()

        self.op = op
        self.expr = expr

    def generate_xml(self):
        xml = '<SIGNO value="{0}">'.format(self.op)
        xml += self.expr.generate_xml()
        xml += '</SIGNO>'
        return xml

    def semantic(self):
        self.expr.semantic()

        if self.expr.type in [D_TYPES['float'], D_TYPES['int']]:
            self.type = self.expr.type
            return

        raise SemError('Can\'t apply unary operator to invalid type')

    def generate_code(self):
        code = self.expr.generate_code()

        if self.op == '-':
            code += [
                'pop rax',
                'not rax',
                'add rax, 1',
                'push rax',
            ]

        return code
from node import Node

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

        if self.expr.type in [D_TYPES['error'], D_TYPES['int']]:
            self.type = self.expr.type
            return

        raise SemError('Can\'t apply unary operator to invalid type')

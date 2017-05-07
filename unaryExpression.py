from node import Node

class UnaryExpression(Node):
    def __init__(self, op, expr):
        super(UnaryExpression, self).__init__()

        self.op = op
        self.expr = expr

    def generateXML(self):
        xml = '<SIGNO value="{0}">'.format(self.op)
        xml += self.expr.generateXML()
        xml += '</SIGNO>'
        return xml

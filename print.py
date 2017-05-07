from node import Node
from dataTypes import D_TYPES

class Print(Node):
    def __init__(self, expr):
        super(Print, self).__init__()
        self.expr = expr

    def generateXML(self):
        xml = '<IMPRIME><EXPRESION>'
        xml += self.expr.generateXML()
        xml += '</EXPRESION></IMPRIME>'
        return xml

    def semantic(self):
        self.expr.semantic()

        if self.expr.type == D_TYPES['error']:
            raise SemError('Invalid print expression')
            return

        self.type = D_TYPES['void']

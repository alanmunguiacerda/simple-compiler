from node import Node
from dataTypes import D_TYPES
from errorManager import SemError

class IfStatement(Node):
    def __init__(self, expr, stm, elseStm):
        super(IfStatement, self).__init__()
        self.expr = expr
        self.stm = stm
        self.elseStm = elseStm

    def generateXML(self):
        xml = '<SI>'
        xml += self.expr.generateXML()
        xml += self.cascadeXML(self.stm)
        if self.elseStm:
            xml += '<OTRO>'
            xml += self.cascadeXML(self.elseStm, False)
            xml += '</OTRO>'
        xml += '</SI>'
        return xml

    def semantic(self):
        self.expr.semantic()
        self.cascadeSemantic(self.stm)
        self.cascadeSemantic(self.elseStm)

        if self.expr.type == D_TYPES['error']:
            raise SemError('Invalid if expression')
            return

        self.type = D_TYPES['void']

from node import Node
from dataTypes import D_TYPES
from errorManager import SemError

class IfStatement(Node):
    def __init__(self, expr, stm, elseStm):
        super(IfStatement, self).__init__()
        self.expr = expr
        self.stm = stm
        self.elseStm = elseStm

    def generate_xml(self):
        xml = '<SI>'
        xml += self.expr.generate_xml()
        xml += self.cascade_xml(self.stm)
        if self.elseStm:
            xml += '<OTRO>'
            xml += self.cascade_xml(self.elseStm, False)
            xml += '</OTRO>'
        xml += '</SI>'
        return xml

    def semantic(self):
        self.expr.semantic()
        self.cascade_semantic(self.stm)
        self.cascade_semantic(self.elseStm)

        if self.expr.type == D_TYPES['error']:
            raise SemError('Invalid if expression')
            return

        self.type = D_TYPES['void']

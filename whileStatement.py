from node import Node
from dataTypes import D_TYPES
from errorManager import SemError

class WhileStatement(Node):
    def __init__(self, expr, stm):
        super(WhileStatement, self).__init__()

        self.expr = expr
        self.stm = stm

    def generateXML(self):
        xml = '<MIENTRAS>'
        xml += self.expr.generateXML()
        xml += self.cascadeXML(self.stm)
        xml += '</MIENTRAS>'
        return xml

    def semantic(self):
        self.expr.semantic()
        self.cascadeSemantic(self.stm)

        if self.expr.type not in [D_TYPES['int'], D_TYPES['float']]:
            raise SemError('Invalid while expression')
            return

        self.type = D_TYPES['void']

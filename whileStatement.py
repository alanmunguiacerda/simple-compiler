from node import Node

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

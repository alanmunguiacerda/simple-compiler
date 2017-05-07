from node import Node

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

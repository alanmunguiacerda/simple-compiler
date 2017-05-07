from node import Node

class Print(Node):
    def __init__(self, expr):
        super(Print, self).__init__()
        self.expr = expr

    def generateXML(self):
        xml = '<IMPRIME><EXPRESION>'
        xml += self.expr.generateXML()
        xml += '</EXPRESION></IMPRIME>'
        return xml

from node import Node
from dataTypes import REL_OP_MAP, OP_MAP

class BinaryExpression(Node):
    def __init__(self, op, left, right):
        super(BinaryExpression, self).__init__()
        self.op = op
        self.left = left
        self.right = right

    def generateXML(self):
        if self.op == '=':
            label = 'ASIGNACION'
            val = ''
        elif self.op in REL_OP_MAP:
            label = 'EXPRESION'
            val = ' value="{0}"'.format(REL_OP_MAP[self.op])
        elif self.op in OP_MAP:
            label = OP_MAP[self.op]
            val = ' value="{0}"'.format(self.op)
        xml = '<{0}{1}>'.format(label, val)
        xml += self.left.generateXML()
        xml += self.right.generateXML()
        xml += '</{0}>'.format(label)
        return xml

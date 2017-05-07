from node import Node
from dataTypes import D_TYPES

class Integer(Node):
    def __init__(self, symbol):
        super(Integer, self).__init__(symbol)
        self.type = D_TYPES['int']

    def generateXML(self):
        return '<ENTERO>{0}</ENTERO>'.format(self.symbol)

    def semantic(self):
        pass

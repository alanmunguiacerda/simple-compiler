from node import Node
from dataTypes import D_TYPES

class Float(Node):
    def __init__(self, symbol):
        super(Float, self).__init__(symbol)
        self.type = D_TYPES['float']

    def generate_xml(self):
        return '<REAL>{0}</REAL>'.format(self.symbol)

    def semantic(self):
        pass

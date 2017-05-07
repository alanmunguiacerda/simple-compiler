from node import Node

class Float(Node):
    def __init__(self, symbol):
        super(Float, self).__init__(symbol)

    def generateXML(self):
        return '<REAL>{0}</REAL>'.format(self.symbol)

from node import Node

class Integer(Node):
    def __init__(self, symbol):
        super(Integer, self).__init__(symbol)

    def generateXML(self):
        return '<ENTERO>{0}</ENTERO>'.format(self.symbol)

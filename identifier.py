from node import Node

class Identifier(Node):
    def __init__(self, identifier):
        super(Identifier, self).__init__(identifier)

    def generateXML(self):
        return '<ID>{0}</ID>'.format(self.symbol)

from node import Node

class Declaration(Node):
    def __init__(self, data_type, declarator):
        super(Declaration, self).__init__()

        self.data_type = data_type
        self.declarator = declarator

    def generateXML(self):
        xml = '<DEFVAR>'
        xml += self.data_type.generateXML()
        xml += self.cascadeXML(self.declarator, False)
        xml += '</DEFVAR>'
        return xml

    def semantic(self):
        data_type = self.data_type.type
        self.cascadeSemantic(self.declarator, data_type)

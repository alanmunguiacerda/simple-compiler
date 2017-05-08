from node import Node

class Declaration(Node):
    def __init__(self, data_type, declarator):
        super(Declaration, self).__init__()

        self.data_type = data_type
        self.declarator = declarator

    def generate_xml(self):
        xml = '<DEFVAR>'
        xml += self.data_type.generate_xml()
        xml += self.cascade_xml(self.declarator, False)
        xml += '</DEFVAR>'
        return xml

    def semantic(self):
        data_type = self.data_type.type
        self.cascade_semantic(self.declarator, data_type)

from node import Node

class Declaration(Node):
    def __init__(self, data_type, declarator):
        super(Declaration, self).__init__()

        self.data_type = data_type
        self.declarator = declarator

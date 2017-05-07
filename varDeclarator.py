from node import Node

class VarDeclarator(Node):
    def __init__(self, id):
        super(VarDeclarator, self).__init__()
        self.id = id

from node import Node

class WhileStatement(Node):
    def __init__(self, expr, stm):
        super(WhileStatement, self).__init__()

        self.expr = expr
        self.stm = stm

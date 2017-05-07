from node import Node

class IfStatement(Node):
    def __init__(self, expr, stm, elseStm):
        super(IfStatement, self).__init__()
        self.expr = expr
        self.stm = stm
        self.elseStm = elseStm

from node import Node

class UnaryExpression(Node):
    def __init__(self, op, expr):
        super(UnaryExpression, self).__init__()

        self.op = op
        self.expr = expr

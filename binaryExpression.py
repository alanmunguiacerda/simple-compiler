from node import Node

class BinaryExpression(Node):
    def __init__(self, op, left, right):
        super(BinaryExpression, self).__init__()
        self.op = op
        self.left = left
        self.right = right

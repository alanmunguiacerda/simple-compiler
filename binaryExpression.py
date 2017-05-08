from node import Node
from dataTypes import REL_OP_MAP, OP_MAP
from errorManager import SemError

class BinaryExpression(Node):
    def __init__(self, op, left, right):
        super(BinaryExpression, self).__init__()
        self.op = op
        self.left = left
        self.right = right

    def generate_xml(self):
        if self.op == '=':
            label = 'ASIGNACION'
            val = ''
        elif self.op in REL_OP_MAP:
            label = 'EXPRESION'
            val = ' value="{0}"'.format(REL_OP_MAP[self.op])
        elif self.op in OP_MAP:
            label = OP_MAP[self.op]
            val = ' value="{0}"'.format(self.op)
        xml = '<{0}{1}>'.format(label, val)
        xml += self.left.generate_xml()
        xml += self.right.generate_xml()
        xml += '</{0}>'.format(label)
        return xml

    def semantic(self):
        self.left.semantic()
        self.right.semantic()

        if self.left.type == self.right.type:
            self.type = self.left.type
            return

        raise SemError('Can\'t operate incompatible types')

    def generate_code(self):
        if self.op == '=':
            code = self.right.generate_code()
            in_table = self.sym_table[self.left.symbol]
            assignment = 'mov _{0}, eax'.format(in_table['id']);
            code.append(assignment)
            return code

        code = self.left.generate_code()
        code.append('mov eax, ebx')

from node import Node
from dataTypes import REL_OP_MAP, OP_MAP
from errorManager import SemError

CODE_OP = {
    '+': 'add',
    '-': 'sub',
    '*': 'imul',
    '/': 'idiv',
}

CODE_COMP = {
    '==': 'je',
    '<>': 'jne',
    '>': 'jg',
    '<': 'jl',
    '>=': 'jge',
    '<=': 'jle',
}

ADDITIVE = frozenset(['+', '-'])
MULTIPLICATIVE = frozenset(['*', '/'])
COMPARISION = frozenset(['==', '<>', '>', '<', '>=', '<='])


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
            code += [
                'pop rax',
                'mov [_{0}], rax'.format(in_table['id']),
            ]
            return code

        code = self.left.generate_code()
        code += self.right.generate_code()
        code.append('pop rbx')
        code.append('pop rax')

        if self.op in ADDITIVE:
            code += [
                '{0} rax, rbx'.format(CODE_OP[self.op]),
                'push rax',
            ]
            return code

        if self.op in MULTIPLICATIVE:
            if self.op == '/':
                code.append('mov rdx, 0')
            code += [
                '{0} rbx'.format(CODE_OP[self.op]),
                'push rax',
            ]
            return code

        if self.op in COMPARISION:
            true_label = self.get_unique_label('true')
            end_label = self.get_unique_label('end')

            code += [
                'cmp rax, rbx',
                '{0} {1}'.format(CODE_COMP[self.op], true_label),
                'push 0',
                'jmp {0}'.format(end_label),
                '{0}:'.format(true_label),
                'push 1',
                '{0}:'.format(end_label),
            ]
            return code

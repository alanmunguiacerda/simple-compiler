from node import Node
from dataTypes import D_TYPES
from errorManager import SemError


class WhileStatement(Node):
    def __init__(self, expr, stm):
        super(WhileStatement, self).__init__()

        self.expr = expr
        self.stm = stm

    def generate_xml(self):
        xml = '<MIENTRAS>'
        xml += self.expr.generate_xml()
        xml += self.cascade_xml(self.stm)
        xml += '</MIENTRAS>'
        return xml

    def semantic(self):
        self.expr.semantic()
        self.cascade_semantic(self.stm)

        if self.expr.type not in [D_TYPES['int'], D_TYPES['float']]:
            raise SemError('Invalid while expression')
            return

        self.type = D_TYPES['void']

    def generate_code(self):
        while_label = self.get_unique_label('while')
        end_label = self.get_unique_label('end')

        code = ['{0}:'.format(while_label)]
        code += self.expr.generate_code()

        code += [
            'pop rax',
            'cmp rax, 0',
            'je {0}'.format(end_label),
        ]

        code += self.cascade_code(self.stm)

        code += [
            'jmp {0}'.format(while_label),
            '{0}:'.format(end_label)
        ]

        return code

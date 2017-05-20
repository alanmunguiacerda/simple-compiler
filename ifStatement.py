from node import Node
from dataTypes import D_TYPES
from errorManager import SemError


class IfStatement(Node):
    def __init__(self, expr, stm, else_stm):
        super(IfStatement, self).__init__()
        self.expr = expr
        self.stm = stm
        self.else_stm = else_stm

    def generate_xml(self):
        xml = '<SI>'
        xml += self.expr.generate_xml()
        xml += self.cascade_xml(self.stm)
        if self.else_stm:
            xml += '<OTRO>'
            xml += self.cascade_xml(self.else_stm, False)
            xml += '</OTRO>'
        xml += '</SI>'
        return xml

    def semantic(self):
        self.expr.semantic()
        self.cascade_semantic(self.stm)
        self.cascade_semantic(self.else_stm)

        if self.expr.type == D_TYPES['error']:
            raise SemError('Invalid if expression')
            return

        self.type = D_TYPES['void']

    def generate_code(self):
        code = self.expr.generate_code()
        code.append('pop rax')

        true_code = self.cascade_code(self.stm)
        else_code = self.cascade_code(self.else_stm)

        else_label = self.get_unique_label('else')
        end_label = self.get_unique_label('end')

        code += [
            'cmp rax, 0',
            'je {0}'.format(else_label),
            '; IF------------',
        ]

        code += true_code

        code += [
            'jmp {0}'.format(end_label),
            '{0}:'.format(else_label),
        ]

        code += else_code

        code += ['{0}:'.format(end_label)]

        return code

from node import Node
from errorManager import SemError


class Identifier(Node):
    def __init__(self, identifier):
        super(Identifier, self).__init__(identifier)

    def generate_xml(self):
        return '<ID>{0}</ID>'.format(self.symbol)

    def semantic(self):
        in_table = self.sym_table.get(self.symbol, False)

        if not in_table:
            raise SemError('Undeclared variable {0}'.format(self.symbol))
            return

        self.type = in_table['data_type']

    def generate_code(self):
        return [
            'mov rax, [_{0}]'.format(self.symbol),
            'push rax',
        ]

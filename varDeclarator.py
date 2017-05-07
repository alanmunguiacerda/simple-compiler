from node import Node
from errorManager import SemError
from dataTypes import D_TYPES

class VarDeclarator(Node):
    def __init__(self, id):
        super(VarDeclarator, self).__init__()
        self.id = id

    def generateXML(self):
        return self.id.generateXML()

    def semantic(self, var_type):
        if self.sym_table.get(self.id.symbol, False):
            raise SemError('Variable {0} already declared'.format(self.id.symbol))
            return

        if var_type not in [D_TYPES['int'], D_TYPES['float']]:
            raise SemError('Variable {0} can\'t be of invalid type')
            return

        self.sym_table[self.id.symbol] = {
            'data_type': var_type,
            'id': self.id.symbol,
        }
        self.type = D_TYPES['void']

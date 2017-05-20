from dataTypes import D_TYPES, TYPES_MAP
from node import Node


class DataType(Node):
    def __init__(self, symbol):
        super(DataType, self).__init__(symbol)
        self.type = self.get_data_type()

    def get_data_type(self):
        return TYPES_MAP.get(self.symbol, D_TYPES['error'])

    def generate_xml(self):
        return '<TIPO>{0}</TIPO>'.format(self.symbol)

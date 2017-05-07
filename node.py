import json

from dataTypes import D_TYPES

class Node:
    def __init__(self, symbol = ''):
        self.symbol = symbol
        self.next = None
        self.type = D_TYPES['error']
        self.name = type(self).__name__

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

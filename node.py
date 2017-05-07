import json

from dataTypes import D_TYPES

class Node:
    sym_table = {}

    def __init__(self, symbol = ''):
        self.symbol = symbol
        self.next = None
        self.type = D_TYPES['error']
        self.name = type(self).__name__

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)

    def generateXML(self):
        xml = '<{0}>'.format(str(type(self).__name__))
        if (self.next):
            xml += self.next.generateXML()
        xml += '</{0}>'.format(str(type(self).__name__))
        return xml

    def cascadeXML(self, obj, block_tag = True):
        curr = obj
        xml = ''
        if block_tag:
            xml = '<BLOQUE>'
        while (curr):
            xml += curr.generateXML()
            curr = curr.next
        if block_tag:
            xml += '</BLOQUE>'
        return xml

    def semantic(self):
        print('Checking {0}'.format(self.name))

    def cascadeSemantic(self, obj, *args):
        curr = obj
        while (curr):
            curr.semantic(*args)
            curr = curr.next

    def generateCode(self):
        return '; Implement this, lol'

def generateXML(tree):
    xml = '<PROGRAMA>'
    xml += tree.cascadeXML(tree, False)
    xml += '</PROGRAMA>'
    return xml

def writeXML(xml):
    file = open('salida.xml', 'w')
    file.write(xml)
    file.close()

def check_semantic(tree):
    tree.cascadeSemantic(tree)

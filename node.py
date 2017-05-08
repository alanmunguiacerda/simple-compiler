import json

from dataTypes import D_TYPES

class Node:
    sym_table = {}

    def __init__(self, symbol = ''):
        self.symbol = symbol
        self.next = None
        self.type = D_TYPES['error']
        self.name = type(self).__name__

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)

    def generate_xml(self):
        xml = '<{0}>'.format(str(type(self).__name__))
        if (self.next):
            xml += self.next.generate_xml()
        xml += '</{0}>'.format(str(type(self).__name__))
        return xml

    def cascade_xml(self, obj, block_tag = True):
        curr = obj
        xml = ''
        if block_tag:
            xml = '<BLOQUE>'
        while (curr):
            xml += curr.generate_xml()
            curr = curr.next
        if block_tag:
            xml += '</BLOQUE>'
        return xml

    def semantic(self):
        print('Checking {0}'.format(self.name))

    def cascade_semantic(self, obj, *args):
        curr = obj
        while (curr):
            curr.semantic(*args)
            curr = curr.next

    def generate_code(self):
        return ['; Implement this, lol']

    def cascade_code(self, obj):
        curr = obj
        code = []
        while (curr):
            code += curr.generate_code()
            curr = curr.next
        return code

    def generate_var_dclr(self, tree):
        code = []
        for k, v in self.sym_table.items():
            new = '_{0} dd 0'.format(v['id'])
            code.append(new)
        return code


def generate_xml(tree):
    xml = '<PROGRAMA>'
    xml += tree.cascade_xml(tree, False)
    xml += '</PROGRAMA>'
    return xml

def write_xml(xml):
    file = open('salida.xml', 'w')
    file.write(xml)
    file.close()

def check_semantic(tree):
    tree.cascade_semantic(tree)

def generate_code(tree):
    code = ['.386', '.model flat, stdcall', 'include', 'include lib', '.data']
    code += tree.generate_var_dclr(tree)
    code += ['.code', 'inicio:']
    code += tree.cascade_code(tree)
    code += ['exit', 'end inicio']
    return '\n'.join(code)

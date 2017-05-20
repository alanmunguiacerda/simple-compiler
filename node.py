import json

from dataTypes import D_TYPES


class Node:
    sym_table = {}
    counters = {
        'true': 0,
        'false': 0,
        'while': 0,
        'if': 0,
        'end': 0,
        'else': 0,
    }

    def __init__(self, symbol=''):
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

    def cascade_xml(self, obj, block_tag=True):
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
            new = '_{0}: resq 1'.format(v['id'])
            code.append(new)
        return code

    def get_unique_label(self, label_type):
        counter = self.counters[label_type]
        self.counters[label_type] += 1
        return '{0}_{1}'.format(label_type, counter)


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
    code = [
        'extern printf',
        'SECTION .data',
        'fmt: db "%d", 10, 0',
        'SECTION .bss'
    ]
    code += tree.generate_var_dclr(tree)
    code += [
        'SECTION .text',
        'global main',
        'main:',
        'push rbp',
        '; PROGRAM START',
    ]
    code += tree.cascade_code(tree)
    code += [
        '; PROGRAM END',
        'pop rbp',
        'mov rax, 0',
        'ret',
    ]
    return '\n'.join(code)


def write_code(code):
    file = open('nasm/salida.asm', 'w')
    file.write(code)
    file.close()

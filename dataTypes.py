D_TYPES = {
    'error': -1,
    'int': 1,
    'float': 2,
}

TYPES_MAP = {
    'entero': D_TYPES['int'],
    'real': D_TYPES['float'],
}

REL_OP_MAP = {
    '=': None,
    '>': '&gt;',
    '<': '&lt;',
    '>=': '&gt;=',
    '<=': '&lt;=',
    '==': '==',
    '<>': '&lt;&gt;',
}

OP_MAP = {
    '+': 'SUMA',
    '-': 'SUMA',
    '*': 'MULT',
    '/': 'MULT',
}

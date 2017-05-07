import re

RES_WORDS = frozenset([
    'imprime',
    'mientras',
    'si',
    'otro',
    'entero',
    'real',
])

NEWLN = 'NEWLN'
SPACE = 'SPACE'
INT = 'INT'
FLOAT = 'FLOAT'
DELIMI = 'DELIMI'
OP_LOG = 'OP_LOG'
OP_ARI = 'OP_ARI'
OP_REL = 'OP_REL'
ASSIGN = 'ASSIGN'
RESERV = 'RESERV'
IDENTI = 'IDENTI'

RE_NEWLN = '[\n|\r\n]+'
RE_SPACE = '[\s\t]+'
RE_FLOAT = '(\d+\.\d+)'
RE_INT = '\d+'
RE_OP_LOG = '\b(y|o)\b'
RE_OP_ARI = '(\+|-|\*|/)'
RE_OP_REL = '(<=|>=|<>|<|>|==)'
RE_ASSIGN = '(=)'
RE_DELIMI = '(\(|\)|\{|\}|;|,)'
RE_IDENTI = '([A-Za-z_])(([A-Za-z0-9_])*)'

patterns = [
    '(?P<{0}>{1})'.format(NEWLN, RE_NEWLN),
    '(?P<{0}>{1})'.format(SPACE, RE_SPACE),
    '(?P<{0}>{1})'.format(FLOAT, RE_FLOAT),
    '(?P<{0}>{1})'.format(INT, RE_INT),
    '(?P<{0}>{1})'.format(OP_LOG, RE_OP_LOG),
    '(?P<{0}>{1})'.format(OP_ARI, RE_OP_ARI),
    '(?P<{0}>{1})'.format(OP_REL, RE_OP_REL),
    '(?P<{0}>{1})'.format(ASSIGN, RE_ASSIGN),
    '(?P<{0}>{1})'.format(DELIMI, RE_DELIMI),
    '(?P<{0}>{1})'.format(IDENTI, RE_IDENTI)
]

token_pattern = r'|'.join(patterns);

TOKEN_PATTERN = re.compile(token_pattern, re.VERBOSE)

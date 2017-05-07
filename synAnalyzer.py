from errorManager import SynError
from tokenPatterns import IDENTI, FLOAT, INT, OP_REL, END_TOKEN
from dataType import DataType
from identifier import Identifier
from varDeclarator import VarDeclarator
from declaration import Declaration
from integer import Integer
from float import Float
from binaryExpression import BinaryExpression
from unaryExpression import UnaryExpression
from print import Print
from whileStatement import WhileStatement
from ifStatement import IfStatement

class Syn:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.lookahead = None

    def next(self):
        if self.current == len(self.tokens):
            return self.lookahead

        self.lookahead = self.tokens[self.current]
        self.current += 1
        return self.lookahead

    def match_t(self, token):
        if token != self.lookahead[0]:
            raise SynError('Expected <{0}> got <{1}>'.format(token, self.lookahead[1]))
        self.next()

    def match_l(self, lexeme):
        if lexeme != self.lookahead[1]:
            raise SynError('Expected <{0}> got <{1}>'.format(lexeme, self.lookahead[1]))
        self.next()

    def l_is(self, *must_be):
        return self.lookahead[1] in must_be

    def t_is(self, *must_be):
        return self.lookahead[0] in must_be

    def analyze(self):
        self.next()
        tree = self.external()
        self.match_t(END_TOKEN)
        return tree

    def type_especifier(self):
        data_type = DataType(self.lookahead[1])
        self.match_l(self.lookahead[1])

        return data_type

    def external(self):
        node = self.statement()
        if node:
            node.next = self.external()

        return node

    def is_declaration(self):
        data_type = self.type_especifier()
        dec = self.declarator()
        dec.next = self.dclr_list()
        self.match_l(';')

        return Declaration(data_type, dec)

    def dclr_list(self):
        if not self.l_is(','):
            return None

        self.match_l(',')
        node = self.declarator()
        node.next = self.dclr_list()

        return node

    def declarator(self):
        identifier = Identifier(self.lookahead[1])
        self.match_t(IDENTI)
        return VarDeclarator(identifier)

    def else_stm(self):
        if not self.l_is('otro'):
            return None

        self.match_l('otro')
        return self.statement()

    def is_if(self):
        self.match_l('si')
        self.match_l('(')
        expr = self.expression()
        self.match_l(')')
        stm = self.statement()
        else_stm = self.else_stm()

        return IfStatement(expr, stm, else_stm)

    def is_while(self):
        self.match_l('mientras')
        self.match_l('(')
        expr = self.expression()
        self.match_l(')')
        stm = self.statement()

        return WhileStatement(expr, stm)

    def statement_list(self):
        stm = self.statement()
        if stm:
            stm.next = self.statement_list()

        return stm

    def is_multi_stm(self):
        self.match_l('{')
        stm_list = self.statement_list()
        self.match_l('}')

        return stm_list

    def is_print(self):
        self.match_l('imprime')
        self.match_l('(')
        expr = self.expression()
        self.match_l(')')
        self.match_l(';')

        return Print(expr)

    def statement(self):
        if self.l_is('si'):
            return self.is_if()

        if self.l_is('mientras'):
            return self.is_while()

        if self.l_is('entero', 'real'):
            return self.is_declaration()

        if self.l_is('imprime'):
            return self.is_print()

        if self.l_is('{'):
            return self.is_multi_stm()

        if self.l_is('(') or self.t_is(IDENTI, INT, FLOAT):
            node = self.expression()
            self.match_l(';')
            return node

        return None

    def is_assignment(self):
        id = Identifier(self.lookahead[1])
        self.match_t(IDENTI)
        self.match_l('=')
        value = self.or_expr()

        return BinaryExpression('=', id, value)

    def expression(self):
        next_tok = self.tokens[self.current]

        if self.t_is(IDENTI) and next_tok[1] == '=':
            return self.is_assignment()

        return self.or_expr()

    def or_expr(self):
        expr = self.and_expr()
        while (self.l_is('o')):
            self.match_l('o')
            expr = BinaryExpression('o', expr, self.and_expr())

        return expr

    def and_expr(self):
        expr = self.eq_expr()
        while (self.l_is('y')):
            self.match_l('y')
            expr = BinaryExpression('y', expr, self.eq_expr())

        return expr

    def eq_expr(self):
        expr = self.rel_expr()
        while (self.l_is('==')):
            self.match_l('==')
            expr = BinaryExpression('==', expr, self.rel_expr())

        return expr

    def rel_expr(self):
        expr = self.add_expr()
        if (self.t_is(OP_REL)):
            op = self.lookahead[1]
            self.match_t(OP_REL)
            expr = BinaryExpression(op, expr, self.add_expr())

        return expr

    def add_expr(self):
        expr = self.mul_expr()
        while (self.l_is('+', '-')):
            op = self.lookahead[1]
            self.match_l(op)
            expr = BinaryExpression(op, expr, self.mul_expr())

        return expr

    def mul_expr(self):
        expr = self.un_expr()
        while (self.l_is('*', '/')):
            op = self.lookahead[1]
            self.match_l(op)
            expr = BinaryExpression(op, expr, self.un_expr())

        return expr

    def un_expr(self):
        if self.l_is('+', '-'):
            op = self.lookahead[1]
            self.match_l(op)
            return UnaryExpression(op, self.un_expr())

        return self.pr_expr()

    def pr_expr(self):
        if self.t_is(IDENTI):
            id = Identifier(self.lookahead[1])
            self.match_t(IDENTI)
            return id

        if self.t_is(INT):
            expr = Integer(self.lookahead[1])
            self.match_t(INT)
            return expr

        if self.t_is(FLOAT):
            expr = Float(self.lookahead[1])
            self.match_t(FLOAT)
            return expr

        self.match_l('(')
        expr = self.expression()
        self.match_l(')')
        return expr

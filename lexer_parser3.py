
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'PRINT', 'STRING', 'LPAREN', 'RPAREN', 'INPUT',
    'ID', 'NUM', 'IGUAL', 'SOMA', 'INT', 'FLOAT', 'DELIM', 'FOR',
    'IF', 'ELSE', 'WHILE', 'DO', 'MAIN', 'IMPORT', 'INCLUDE'
)

t_DELIM = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUAL = r'='
t_SOMA = r'\+'
t_STRING = r'\"([^\\"]|\\.)*\"'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUM = r'\d+'
t_ignore = ' \t\n'

def t_PRINT(t):
    r'System\.out\.println'
    return t

def t_INPUT(t):
    r'JOptionPane\.ShowInputDialog'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_MAIN(t):
    r'(public\s+static\s+void\s+main|def\s+main)'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_INCLUDE(t):
    r'\#include<[^>]+>'
    return t

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_stmt(p):
    '''stmt : PRINT LPAREN STRING RPAREN DELIM
            | INPUT LPAREN STRING RPAREN DELIM
            | INT ID IGUAL NUM DELIM
            | FLOAT ID IGUAL expr DELIM
            | ID IGUAL expr DELIM
            | FOR LPAREN STRING RPAREN
            | IF LPAREN STRING RPAREN
            | ELSE
            | WHILE LPAREN STRING RPAREN
            | DO
            | MAIN LPAREN ID RPAREN
            | IMPORT ID DELIM
            | INCLUDE'''
    print('Comando reconhecido')

def p_expr(p):
    '''expr : ID
            | NUM
            | expr SOMA ID
            | expr SOMA NUM'''
    pass

def p_error(p):
    print("Erro de sintaxe!")

parser = yacc.yacc(write_tables=False)

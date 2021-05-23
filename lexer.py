import ply.lex as lex
import re
from TOKENS import *

states = (
   ('string','exclusive'),
)

tokens = [
    'ASSIGN', 'ID', 'FLOAT_NUM', 'QUOM',
    'STRING', 'TCOMMA', 'COMMA', 'RELOP',
    'OPEN', 'CLOSE', 'INT_NUM', 'PLUSMINUS', 'DIVMULT',
    'CLOSE_CLASS', 'OPEN_CLASS', 'COMMENT', 'COLON'
]

tokens += reserved.values()

t_QUOM = r'"'
t_ANY_VAR = r'[a-z]\w*'
t_ASSIGN = r'\='
t_TCOMMA = r';'
t_COMMA = r','
t_COLON = r':'
t_OPEN = r'\('
t_CLOSE = r'\)'
t_OPEN_CLASS = r'\{'
t_CLOSE_CLASS = r'\}'
t_PLUSMINUS = r'\+|\-'
t_DIVMULT = r'/|\*'
t_RELOP = r'\==|\<=|\>=|\>|\<|\!='


def t_COMMENT(t):
    r'@(\\.|[^@])+@'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_ANY_QUOM(t):
    r'"'
    if t.lexer.current_state() == 'string':
        t.lexer.begin('INITIAL')
    else:
        t.lexer.begin('string')
    return t

def t_FLOAT_NUM(t):
    r'\d+\.\d+'
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    t.value = float(t.value)
    return t

def t_INT_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_string_STRING = r'(\\.|[^$"])+'
t_string_ignore = ''

def t_string_error(t):
    print ("Некорректная строка '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \r\t\f'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print ("Некорректная команда '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.UNICODE | re.DOTALL | re.IGNORECASE)

def main():
    program =  '''
    var int x;
    if ( r < 10 ) then {
        x = x + 1;
    }
    '''

    lexer.input(program)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    main()

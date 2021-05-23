import ply.yacc as yacc
from lexer import tokens


class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

    scope = 'global'


def p_programm(p):
    '''
    programm : var start
             '''
    p[0] = Node('programm', [p[1], p[2]])


def p_identifier_list(p):
    '''identifier_list : ID
                       | identifier_list COMMA ID '''
    if len(p) == 2:
        p[0] = Node("ID", [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_var(p):
    '''var : var VAR type identifier_list TCOMMA
                    | empty'''
    if len(p) == 2:
        p[0] = Node('var', [], )
    else:
        p[0] = p[1].add_parts([p[3], p[4]])


def p_type(p):
    '''type : INT
            | FLOAT
            | STR'''
    p[0] = Node("type", [p[1]])


def p_start(p):
    '''start : statements
            |  empty'''
    p[0] = Node("start", [p[1]])


def p_statements(p):
    '''statements : matched
                  | statements matched'''
    if len(p) == 2:
        p[0] = Node('statements', [p[1]])
        p[1].scope = p[0].scope
    else:
        p[0] = p[1].add_parts([p[2]])


def p_matched(p):
    '''matched : IF OPEN rel CLOSE THEN statement
                 | WHILE OPEN rel CLOSE statement
                 | function_block
                 | rel
                 | write
                 '''
    if len(p) == 2:
        p[0] = p[1]
        p[1].scope = p[0].scope
    elif len(p) == 6:
        p[0] = Node("while", [p[3], p[5]])
    else:
        p[0] = Node('If\Else', [p[3], p[6]])


def p_function_block(p):
    '''function_block : functions
                      | function_block functions'''
    if len(p) == 2:
        p[0] = Node('function_block', [p[1]])
    else:
        p[0] = p[1].add_parts([p[2]])


def p_functions(p):
    '''functions : function var statement'''
    p[0] = Node("functions", [p[1], p[2], p[3]])
    p[2].scope = p[1].scope


def p_function(p):
    '''function : FUNKTION ID args '''
    p[0] = Node("function", [p[1], p[2], p[3]])
    p[3].scope = p[2]
    p[0].scope = p[2]


def p_args(p):
    '''args : OPEN prm CLOSE'''
    p[0] = p[2]
    p[2].scope = p[0].scope


def p_prm(p):
    '''prm : type identifier_list
           | prm TCOMMA type identifier_list'''
    if len(p) == 3:
        p[0] = Node("prm", [p[1], p[2]])
        p[2].scope = p[0].scope
    else:
        p[0] = p[1].add_parts([p[3], p[4]])
        p[4].scope = p[0].scope


def p_statement(p):
    '''statement : OPEN_CLASS start CLOSE_CLASS'''
    p[0] = Node("statement", [p[2]])


def p_expr(p):
    '''expr : rel
            | expr COMMA rel'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("expr", [p[1], p[3]])


def p_rel(p):
    '''rel : NOT unary
            | RETURN unary
            | rel AND unary
            | rel OR unary
            | unary RELOP unary
            | unary'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        if p[1] == "return":
            p[0] = Node(p[1], [p[2]])
        else:
            p[0] = Node("rel", [p[1], p[2]])
    else:
        p[0] = Node("rel", [p[1], p[2], p[3]])


def p_unary(p):
    '''unary : term
            | assign'''
    if len(p) == 2:
        p[0] = Node("unary", [p[1]])


def p_assign(p):
    '''assign : fact ASSIGN term
               | fact'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("assign", [p[1], p[2], p[3]])


def p_term(p):
    '''term : join
            | term PLUSMINUS join'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("term", [p[1], p[2], p[3]])


def p_join(p):
    '''join : fact
            | join DIVMULT fact'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("join", [p[1], p[2], p[3]])


def p_write(p):
    '''write : WRITE OPEN fact CLOSE TCOMMA '''
    p[0] = Node("write", [p[1], p[3]])


def p_read(p):
    '''read : READ OPEN CLOSE TCOMMA'''
    p[0] = Node("read", [p[1]])


def p_fact(p):
    '''fact : ID
              | ID OPEN expr CLOSE
              | INT_NUM
              | CONTINUE
              | BREAK
              | FLOAT_NUM
              | OPEN rel CLOSE
              | type fact
              | NOT fact
              | QUOM STRING QUOM
              | fact TCOMMA
              '''
    if len(p) == 2:
        p[0] = Node("fact", [p[1]])
    elif len(p) == 3:
        if p[2] == ";":
            p[0] = p[1]
        else:
            p[0] = Node("fact", [p[1], p[2]])
    elif len(p) == 4:
        p[0] = Node("fact", [p[1], p[2], p[3]])
    elif len(p) == 5:
        p[0] = Node("func", [p[1], p[3]])


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print('Неизвестный токен:', p)


precedence = (
    ('left', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'PLUSMINUS'),
    ('left', 'DIVMULT'),
)

def get_table(init_prog):
    global simbol_table
    simbol_table = {}
    with open(init_prog, 'r') as f:
        s = f.read()

    result = build_tree(s)
    generateSymbolTable(result)

    return simbol_table

def gen_sem(t):
    global simbol_table
    simbol_table = {}
    generateSymbolTable(t)

    return simbol_table

def generateSymbolTable(tree):
    global simbol_table
    for part in tree.parts:
        if type(part) != str and type(part) != int and type(part) != float:
            if part.type == 'var' or part.type == 'prm':
                for i in part.parts:
                    if i.type == 'type':
                        type_tmp = i.parts[0]
                    if i.type == 'ID':
                        if part.scope not in simbol_table.keys():
                            simbol_table[part.scope] = {}
                            simbol_table[part.scope][type_tmp] = []
                        elif type_tmp not in simbol_table[part.scope].keys():
                            simbol_table[part.scope][type_tmp] = []
                        for j in i.parts:
                            simbol_table[part.scope][type_tmp].append(j)
            generateSymbolTable(part)

def build_tree(code):
    parser = yacc.yacc()
    return parser.parse(code)


if __name__ == "__main__":
    pass
#     data = '''
#     var int b;
# print("Hello");
# b = 2+2;
# print(b);
#     '''
#     result = build_tree(data)
#     print(result)



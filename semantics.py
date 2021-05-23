from parser2 import build_tree
import parser2 as t
import sys

counter_f = 0
counter_t = 0
counter_s = 0
counter_L = 0
counter_str = 1
counter_else = 0
counter_if = 0
counter_main = 0

goto_key_global = ''
list_of_registr = []
list_of_float = []
simbol_table = t.get_table('programm')

def check_existence(part,simbol_table):
    for key in simbol_table:
        for i in simbol_table[key]:
            if ret_fact(part) in simbol_table[key][i]:
                type_var = i
                return type_var
    print('Ошибка компиляции')
    print("Использование необъявленной переменной", ret_fact(part))
    sys.exit()


def ret_fact(leaf):
    if type(leaf) != (str or int or float):
        return leaf.parts[0]
    else:
        return leaf

def ret_class_type(type_var):
    if type_var == 'int':
        return int
    elif type_var == 'float':
        return float

def check_type(leaf1, leaf2, type_var):
    if type(leaf2) == str(ret_class_type(type_var)):
        return True
    else:
        return False

def check_type_float(leaf1, leaf2, type_var):
    if type(leaf2) == ret_class_type(type_var) or str(leaf2)[0] == '_':
        return True
    else:
        False

def check_if_while():
        print('Компиляция провалена')
        print('Ошибка в условии if или while')
        sys.exit()

def sad(part, tmp=0):
    for i in part.parts:
        tmp += 1
    if tmp == 1: return False
    else: return True

def ret_func_args(part):
    tmp_arr = []

    for fcts in part.parts:
        tmp_arr.append(ret_fact(fcts.parts[0]))
    return tmp_arr

# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftASSIGNleftORleftANDleftNOTleftPLUSMINUSleftDIVMULTAND ASSIGN BREAK CLOSE CLOSE_CLASS COLON COMMA COMMENT CONTINUE DIVMULT FLOAT FLOAT_NUM FUNKTION ID IF INT INT_NUM NOT OPEN OPEN_CLASS OR PLUSMINUS QUOM READ RELOP RETURN STR STRING TCOMMA THEN VAR WHILE WRITE\n    programm : var start\n             identifier_list : ID\n                       | identifier_list COMMA ID var : var VAR type identifier_list TCOMMA\n                    | emptytype : INT\n            | FLOAT\n            | STRstart : statements\n            |  emptystatements : matched\n                  | statements matchedmatched : IF OPEN rel CLOSE THEN statement\n                 | WHILE OPEN rel CLOSE statement\n                 | function_block\n                 | rel\n                 | write\n                 function_block : functions\n                      | function_block functionsfunctions : function var statementfunction : FUNKTION ID args args : OPEN prm CLOSEprm : type identifier_list\n           | prm TCOMMA type identifier_liststatement : OPEN_CLASS start CLOSE_CLASSexpr : rel\n            | expr COMMA relrel : NOT unary\n            | RETURN unary\n            | rel AND unary\n            | rel OR unary\n            | unary RELOP unary\n            | unaryunary : term\n            | assignassign : fact ASSIGN term\n               | factterm : join\n            | term PLUSMINUS joinjoin : fact\n            | join DIVMULT factwrite : WRITE OPEN fact CLOSE TCOMMA read : READ OPEN CLOSE TCOMMAfact : ID\n              | ID OPEN expr CLOSE\n              | INT_NUM\n              | CONTINUE\n              | BREAK\n              | FLOAT_NUM\n              | OPEN rel CLOSE\n              | type fact\n              | NOT fact\n              | QUOM STRING QUOM\n              | fact TCOMMA\n              empty :'
    
_lr_action_items = {'VAR':([0,2,3,22,53,74,80,95,],[-55,5,-5,-55,5,-21,-4,-22,]),'IF':([0,2,3,7,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,72,73,78,79,80,88,92,93,94,99,],[-55,10,-5,10,-11,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,10,-39,-41,-53,-4,-45,-14,-42,-25,-13,]),'WHILE':([0,2,3,7,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,72,73,78,79,80,88,92,93,94,99,],[-55,13,-5,13,-11,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,13,-39,-41,-53,-4,-45,-14,-42,-25,-13,]),'NOT':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,17,-5,38,17,-11,17,-16,-15,-17,-18,38,-33,38,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,38,-12,17,38,38,17,-19,-28,-37,38,-29,38,38,-54,38,17,38,-52,-50,-30,-31,-32,-40,-36,-20,17,-39,-41,-53,-4,-45,17,-14,-42,-25,-13,]),'RETURN':([0,2,3,7,9,11,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,40,44,45,46,47,49,52,56,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,19,-5,19,-11,19,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,19,19,-19,-28,-37,-29,-54,19,-52,-50,-30,-31,-32,-40,-36,-20,19,-39,-41,-53,-4,-45,19,-14,-42,-25,-13,]),'WRITE':([0,2,3,7,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,72,73,78,79,80,88,92,93,94,99,],[-55,20,-5,20,-11,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,20,-39,-41,-53,-4,-45,-14,-42,-25,-13,]),'FUNKTION':([0,2,3,7,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,72,73,78,79,80,88,92,93,94,99,],[-55,25,-5,25,-11,-16,25,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,25,-39,-41,-53,-4,-45,-14,-42,-25,-13,]),'ID':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,81,87,88,89,92,93,94,99,100,],[-55,26,-5,26,26,-11,26,-16,-15,-17,-18,26,-33,26,-37,-34,-35,55,-44,-38,-46,-47,-48,-49,-6,-7,-8,60,-51,26,-12,26,26,26,26,-19,-28,-37,26,-29,26,26,-54,26,26,26,-52,-50,-30,-31,-32,-40,-36,-20,26,-39,-41,-53,-4,90,60,-45,26,-14,-42,-25,-13,60,]),'INT_NUM':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,28,-5,28,28,-11,28,-16,-15,-17,-18,28,-33,28,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,28,-12,28,28,28,28,-19,-28,-37,28,-29,28,28,-54,28,28,28,-52,-50,-30,-31,-32,-40,-36,-20,28,-39,-41,-53,-4,-45,28,-14,-42,-25,-13,]),'CONTINUE':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,29,-5,29,29,-11,29,-16,-15,-17,-18,29,-33,29,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,29,-12,29,29,29,29,-19,-28,-37,29,-29,29,29,-54,29,29,29,-52,-50,-30,-31,-32,-40,-36,-20,29,-39,-41,-53,-4,-45,29,-14,-42,-25,-13,]),'BREAK':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,30,-5,30,30,-11,30,-16,-15,-17,-18,30,-33,30,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,30,-12,30,30,30,30,-19,-28,-37,30,-29,30,30,-54,30,30,30,-52,-50,-30,-31,-32,-40,-36,-20,30,-39,-41,-53,-4,-45,30,-14,-42,-25,-13,]),'FLOAT_NUM':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,31,-5,31,31,-11,31,-16,-15,-17,-18,31,-33,31,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,31,-12,31,31,31,31,-19,-28,-37,31,-29,31,31,-54,31,31,31,-52,-50,-30,-31,-32,-40,-36,-20,31,-39,-41,-53,-4,-45,31,-14,-42,-25,-13,]),'OPEN':([0,2,3,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,11,-5,11,11,-11,40,11,-16,44,-15,-17,-18,11,-33,11,50,-37,-34,-35,56,-38,-46,-47,-48,-49,-6,-7,-8,-51,11,-12,11,11,11,11,-19,-28,-37,11,-29,11,11,-54,11,75,11,11,-52,-50,-30,-31,-32,-40,-36,-20,11,-39,-41,-53,-4,-45,11,-14,-42,-25,-13,]),'QUOM':([0,2,3,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,58,61,63,64,65,67,69,70,71,72,73,78,79,80,88,89,92,93,94,99,],[-55,32,-5,32,32,-11,32,-16,-15,-17,-18,32,-33,32,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,32,-12,32,32,32,32,-19,-28,-37,32,-29,32,32,-54,32,32,32,79,-52,-50,-30,-31,-32,-40,-36,-20,32,-39,-41,-53,-4,-45,32,-14,-42,-25,-13,]),'INT':([0,2,3,5,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,75,78,79,80,88,89,92,93,94,96,99,],[-55,33,-5,33,33,33,-11,33,-16,-15,-17,-18,33,-33,33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,33,-12,33,33,33,33,-19,-28,-37,33,-29,33,33,-54,33,33,33,-52,-50,-30,-31,-32,-40,-36,-20,33,-39,33,-41,-53,-4,-45,33,-14,-42,-25,33,-13,]),'FLOAT':([0,2,3,5,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,75,78,79,80,88,89,92,93,94,96,99,],[-55,34,-5,34,34,34,-11,34,-16,-15,-17,-18,34,-33,34,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,34,-12,34,34,34,34,-19,-28,-37,34,-29,34,34,-54,34,34,34,-52,-50,-30,-31,-32,-40,-36,-20,34,-39,34,-41,-53,-4,-45,34,-14,-42,-25,34,-13,]),'STR':([0,2,3,5,6,7,9,11,12,14,15,16,17,18,19,21,23,24,26,27,28,29,30,31,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,54,56,57,61,63,64,65,67,69,70,71,72,73,75,78,79,80,88,89,92,93,94,96,99,],[-55,35,-5,35,35,35,-11,35,-16,-15,-17,-18,35,-33,35,-37,-34,-35,-44,-38,-46,-47,-48,-49,-6,-7,-8,-51,35,-12,35,35,35,35,-19,-28,-37,35,-29,35,35,-54,35,35,35,-52,-50,-30,-31,-32,-40,-36,-20,35,-39,35,-41,-53,-4,-45,35,-14,-42,-25,35,-13,]),'$end':([0,1,2,3,4,7,8,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,73,78,79,80,88,92,93,94,99,],[-55,0,-55,-5,-1,-9,-10,-11,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,-39,-41,-53,-4,-45,-14,-42,-25,-13,]),'OPEN_CLASS':([3,22,53,74,80,83,91,95,],[-5,-55,72,-21,-4,72,72,-22,]),'CLOSE_CLASS':([7,8,9,12,14,15,16,18,21,23,24,26,27,28,29,30,31,37,39,45,46,47,49,52,61,63,64,65,67,69,70,71,72,73,78,79,85,88,92,93,94,99,],[-9,-10,-11,-16,-15,-17,-18,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-12,-19,-28,-37,-29,-54,-52,-50,-30,-31,-32,-40,-36,-20,-55,-39,-41,-53,94,-45,-14,-42,-25,-13,]),'AND':([12,18,21,23,24,26,27,28,29,30,31,37,41,46,47,49,52,61,62,63,64,65,66,67,69,70,73,77,78,79,88,98,],[42,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,42,-28,-37,-29,-54,-52,42,-50,-30,-31,42,-32,-40,-36,-39,42,-41,-53,-45,42,]),'OR':([12,18,21,23,24,26,27,28,29,30,31,37,41,46,47,49,52,61,62,63,64,65,66,67,69,70,73,77,78,79,88,98,],[43,-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,43,-28,-37,-29,-54,-52,43,-50,-30,-31,43,-32,-40,-36,-39,43,-41,-53,-45,43,]),'RELOP':([18,21,23,24,26,27,28,29,30,31,37,47,52,61,63,69,70,73,78,79,88,],[48,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-52,-54,-52,-50,-40,-36,-39,-41,-53,-45,]),'CLOSE':([18,21,23,24,26,27,28,29,30,31,37,41,46,47,49,52,60,61,62,63,64,65,66,67,68,69,70,73,76,77,78,79,86,88,90,97,98,101,],[-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,63,-28,-37,-29,-54,-2,-52,82,-50,-30,-31,83,-32,84,-40,-36,-39,88,-26,-41,-53,95,-45,-3,-23,-27,-24,]),'COMMA':([18,21,23,24,26,27,28,29,30,31,37,46,47,49,52,59,60,61,63,64,65,67,69,70,73,76,77,78,79,88,90,97,98,101,],[-33,-37,-34,-35,-44,-38,-46,-47,-48,-49,-51,-28,-37,-29,-54,81,-2,-52,-50,-30,-31,-32,-40,-36,-39,89,-26,-41,-53,-45,-3,81,-27,81,]),'ASSIGN':([21,26,28,29,30,31,37,47,52,61,63,79,88,],[51,-44,-46,-47,-48,-49,-51,-52,-54,-52,-50,-53,-45,]),'DIVMULT':([21,26,27,28,29,30,31,37,47,52,61,63,69,73,78,79,88,],[-40,-44,57,-46,-47,-48,-49,-51,-40,-54,-52,-50,-40,57,-41,-53,-45,]),'PLUSMINUS':([21,23,26,27,28,29,30,31,37,47,52,61,63,69,70,73,78,79,88,],[-40,54,-44,-38,-46,-47,-48,-49,-51,-40,-54,-52,-50,-40,54,-39,-41,-53,-45,]),'TCOMMA':([21,26,28,29,30,31,37,47,52,59,60,61,63,68,69,78,79,84,86,88,90,97,101,],[52,-44,-46,-47,-48,-49,52,-52,-54,80,-2,-52,-50,52,52,52,-53,93,96,-45,-3,-23,-24,]),'STRING':([32,],[58,]),'THEN':([82,],[91,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programm':([0,],[1,]),'var':([0,22,],[2,53,]),'empty':([0,2,22,72,],[3,8,3,8,]),'start':([2,72,],[4,85,]),'type':([2,5,6,7,11,17,19,38,40,42,43,44,48,50,51,54,56,57,72,75,89,96,],[6,36,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,87,6,100,]),'statements':([2,72,],[7,7,]),'matched':([2,7,72,],[9,39,9,]),'rel':([2,7,11,40,44,56,72,89,],[12,12,41,62,66,77,12,98,]),'function_block':([2,7,72,],[14,14,14,]),'write':([2,7,72,],[15,15,15,]),'functions':([2,7,14,72,],[16,16,45,16,]),'unary':([2,7,11,17,19,40,42,43,44,48,56,72,89,],[18,18,18,46,49,18,64,65,18,67,18,18,18,]),'fact':([2,6,7,11,17,19,38,40,42,43,44,48,50,51,54,56,57,72,89,],[21,37,21,21,47,21,61,21,21,21,21,21,68,69,69,21,78,21,21,]),'function':([2,7,14,72,],[22,22,22,22,]),'term':([2,7,11,17,19,40,42,43,44,48,51,56,72,89,],[23,23,23,23,23,23,23,23,23,23,70,23,23,23,]),'assign':([2,7,11,17,19,40,42,43,44,48,56,72,89,],[24,24,24,24,24,24,24,24,24,24,24,24,24,]),'join':([2,7,11,17,19,40,42,43,44,48,51,54,56,72,89,],[27,27,27,27,27,27,27,27,27,27,27,73,27,27,27,]),'identifier_list':([36,87,100,],[59,97,101,]),'statement':([53,83,91,],[71,92,99,]),'args':([55,],[74,]),'expr':([56,],[76,]),'prm':([75,],[86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programm","S'",1,None,None,None),
  ('programm -> var start','programm',2,'p_programm','parser2.py',28),
  ('identifier_list -> ID','identifier_list',1,'p_identifier_list','parser2.py',34),
  ('identifier_list -> identifier_list COMMA ID','identifier_list',3,'p_identifier_list','parser2.py',35),
  ('var -> var VAR type identifier_list TCOMMA','var',5,'p_var','parser2.py',43),
  ('var -> empty','var',1,'p_var','parser2.py',44),
  ('type -> INT','type',1,'p_type','parser2.py',52),
  ('type -> FLOAT','type',1,'p_type','parser2.py',53),
  ('type -> STR','type',1,'p_type','parser2.py',54),
  ('start -> statements','start',1,'p_start','parser2.py',59),
  ('start -> empty','start',1,'p_start','parser2.py',60),
  ('statements -> matched','statements',1,'p_statements','parser2.py',65),
  ('statements -> statements matched','statements',2,'p_statements','parser2.py',66),
  ('matched -> IF OPEN rel CLOSE THEN statement','matched',6,'p_matched','parser2.py',75),
  ('matched -> WHILE OPEN rel CLOSE statement','matched',5,'p_matched','parser2.py',76),
  ('matched -> function_block','matched',1,'p_matched','parser2.py',77),
  ('matched -> rel','matched',1,'p_matched','parser2.py',78),
  ('matched -> write','matched',1,'p_matched','parser2.py',79),
  ('function_block -> functions','function_block',1,'p_function_block','parser2.py',91),
  ('function_block -> function_block functions','function_block',2,'p_function_block','parser2.py',92),
  ('functions -> function var statement','functions',3,'p_functions','parser2.py',100),
  ('function -> FUNKTION ID args','function',3,'p_function','parser2.py',106),
  ('args -> OPEN prm CLOSE','args',3,'p_args','parser2.py',113),
  ('prm -> type identifier_list','prm',2,'p_prm','parser2.py',119),
  ('prm -> prm TCOMMA type identifier_list','prm',4,'p_prm','parser2.py',120),
  ('statement -> OPEN_CLASS start CLOSE_CLASS','statement',3,'p_statement','parser2.py',130),
  ('expr -> rel','expr',1,'p_expr','parser2.py',135),
  ('expr -> expr COMMA rel','expr',3,'p_expr','parser2.py',136),
  ('rel -> NOT unary','rel',2,'p_rel','parser2.py',144),
  ('rel -> RETURN unary','rel',2,'p_rel','parser2.py',145),
  ('rel -> rel AND unary','rel',3,'p_rel','parser2.py',146),
  ('rel -> rel OR unary','rel',3,'p_rel','parser2.py',147),
  ('rel -> unary RELOP unary','rel',3,'p_rel','parser2.py',148),
  ('rel -> unary','rel',1,'p_rel','parser2.py',149),
  ('unary -> term','unary',1,'p_unary','parser2.py',162),
  ('unary -> assign','unary',1,'p_unary','parser2.py',163),
  ('assign -> fact ASSIGN term','assign',3,'p_assign','parser2.py',169),
  ('assign -> fact','assign',1,'p_assign','parser2.py',170),
  ('term -> join','term',1,'p_term','parser2.py',178),
  ('term -> term PLUSMINUS join','term',3,'p_term','parser2.py',179),
  ('join -> fact','join',1,'p_join','parser2.py',187),
  ('join -> join DIVMULT fact','join',3,'p_join','parser2.py',188),
  ('write -> WRITE OPEN fact CLOSE TCOMMA','write',5,'p_write','parser2.py',196),
  ('read -> READ OPEN CLOSE TCOMMA','read',4,'p_read','parser2.py',201),
  ('fact -> ID','fact',1,'p_fact','parser2.py',206),
  ('fact -> ID OPEN expr CLOSE','fact',4,'p_fact','parser2.py',207),
  ('fact -> INT_NUM','fact',1,'p_fact','parser2.py',208),
  ('fact -> CONTINUE','fact',1,'p_fact','parser2.py',209),
  ('fact -> BREAK','fact',1,'p_fact','parser2.py',210),
  ('fact -> FLOAT_NUM','fact',1,'p_fact','parser2.py',211),
  ('fact -> OPEN rel CLOSE','fact',3,'p_fact','parser2.py',212),
  ('fact -> type fact','fact',2,'p_fact','parser2.py',213),
  ('fact -> NOT fact','fact',2,'p_fact','parser2.py',214),
  ('fact -> QUOM STRING QUOM','fact',3,'p_fact','parser2.py',215),
  ('fact -> fact TCOMMA','fact',2,'p_fact','parser2.py',216),
  ('empty -> <empty>','empty',0,'p_empty','parser2.py',232),
]

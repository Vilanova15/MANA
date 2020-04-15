import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN

tokens = (
    'CHARACTER', 
    'DIGIT', 
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'EQ',
    'QUOM',
    'STRING',
)

reserved = {
    'init': 'INIT',
    'as': 'AS',
    'Scene': 'SCENE',
    'Option': 'OPTION',
    'Item': 'ITEM',
    'name': 'NAME',
    'desc': 'DESC',
    'display_scene': 'DISPLAY_SCENE',
    'display_option': 'DISPLAY_OPTION',
    'add_option': 'ADD_OPTION',
    'add_next_scene': 'ADD_NEXT_SCENE',
    'get_option_input': 'GET_OPTION_INPUT'
}

tokens = tokens + tuple(reserved.values())

t_CHARACTER = r'[a-zA-Z_]'
t_DIGIT = r'[0-9]'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQ = r'='
t_QUOM = r'\"'

identifier = r'(' + t_CHARACTER + r'(' + t_CHARACTER + r'|' + t_DIGIT + r')*)'
string = r'(' + t_QUOM + r'(.)*' + t_QUOM + r')'

@TOKEN(identifier)
def t_ID(t):
    t.type = reserved.get(t.value,'ID')
    return t

@TOKEN(string)
def t_STRING(t):
    return t

t_ignore_TAB = r'\t'
t_ignore_COMMENT = r'\#.*'
t_ignore_NEWLINE = r'\n+'
t_ignore_WHITESPACE = r'\s'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
      
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = """
init shrine_entrance as Scene (
	name = "Shrine Entrance",
	desc = "A shrine"
);

init attack_guard as Option (
	name = "Attack the guard",
	desc = "You change in! No time for questions!"
);

init run_away as Option (
	name = "Run away in terror"
	desc = "You turn back and run as fast as you can."
);

init approach_guard as Option (
	name = "Approach the guard carefully",
	desc = "You cautiously approach the skeleton guard."
);

init guard_parries as Scene (
	name = "Guard parries",
	desc = "The skeleton guard reacts with swift movements."
);

add_option attack_guard to guard_parries;

add_next_scene guard_parries to shrine_entrance;

init back_at_village as Scene (
	name = "Back at village",
	desc = "You find yourself back in the village."
);

add_option run_away to back_at_village;
add_next_scene back_at_village to shrine_entrance;
"""

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
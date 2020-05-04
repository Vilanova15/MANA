import sys
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
from .scene import Scene, Option
from .game_engine import GameEngine
# from treelib import Node, Tree

# sceneTree = Tree()
reference_log = {}
initialScene: Scene = None

### ----------------------------------------------------------------------

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
    'to' : 'TO',
    'modify' : 'MODIFY',
    'Scene': 'SCENE',
    'Option': 'OPTION',
    'Item': 'ITEM',
    'name': 'NAME',
    'desc': 'DESC',
    'display_scene': 'DISPLAY_SCENE',
    'display_option': 'DISPLAY_OPTION',
    'add_option': 'ADD_OPTION',
    'add_next_scene': 'ADD_NEXT_SCENE',
    'get_option_input': 'GET_OPTION_INPUT',
    'quit' : 'QUIT'
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


#---------------------------------------------------------

def p_Main(p):
    """
    Main : ExpList
    """
    p[0] = p[1]
    engine = GameEngine()
    engine.run_game(initialScene)

def p_Exp_Init(p):
    """
    Exp : INIT Id AS ObjectDef
    """
    global initialScene
    p[0] = (p[1], p[2], p[4])
    reference_log[p[2]] = p[4]
    if isinstance(p[4], Scene) and initialScene==None:
        initialScene = p[4]

def p_Exp_AddFunc(p):
    """
    Exp : AddFunc Id TO Id SEMICOLON
    """
    p[0] = (p[1], p[2], p[4])
    # try:
    #     child = reference_log[p[2]]
    #     paren = reference_log[p[4]]
    # except:
    #     raise Exception('Object does not exist!')
    child = reference_log[p[2]]
    paren = reference_log[p[4]]
    if p[1] == 'add_next_scene' and isinstance(child, Scene) and isinstance(paren, Scene):
        paren.add_next_scene(child)
    elif p[1] == 'add_option' and isinstance(child, Option) and isinstance(paren, Scene):
        paren.set_option(child)

def p_Exp_Display(p):
    """
    Exp : DisplayFunc Id SEMICOLON
    """
    p[0] = (p[1], p[2])
    obj = reference_log[p[2]]
    if p[1] == 'display_scene' and isinstance(obj, Scene):
        obj.display_scene()
    elif p[1] == 'display_option' and isinstance(obj, Option):
        obj.display_option()

def p_Exp_Modify(p):
    """
    Exp : MODIFY Id Def SEMICOLON
    """
    p[0] = (p[1], p[2], p[3])
    obj = reference_log[p[2]]
    if isinstance(obj, Scene) :
        obj.modify_scene(p[3][0], p[3][1])
    elif isinstance(obj, Option) :
        obj.modify_option(p[3][0], p[3][1])

def p_Exp_Quit(p):
    """
    Exp : Quit
    """
    p[0] = p[1]
    print("Goodbye!")

def p_Exp_Empty(p):
    """
    Exp : Empty
    """
    p[0] = p[1]

def p_ExpList(p):
    """
    ExpList : Exp ExpList
            | Exp
    """
    try:
        p[0] = [p[1]]+p[2]
    except:
        p[0] = [p[1]]

def p_ObjectType(p):
    """
    ObjectType : SCENE
                | OPTION
    """
    p[0] = p[1]

def p_ObjectDef(p):
    """
    ObjectDef : ObjectType Def SEMICOLON
    """
    if p[1] == 'Scene':
        p[0] = Scene(p[2][0], p[2][1])
    elif p[1] == 'Option':
        p[0] = Option(p[2][0], p[2][1])

def p_Def(p):
    """
    Def : LPAREN AttrList RPAREN
    """
    p[0] = p[2]

def p_AttrList(p):
    """
    AttrList : AttrDeclar COMMA AttrList
            | AttrDeclar
    """
    try:
        p[0] = [p[1]]+p[3]
    except:
        p[0] = [p[1]]

def p_AttrDeclar(p):
    """
    AttrDeclar : Attribute EQ StrVal
    """
    p[1] = p[3]
    p[0] = p[1]

def p_StrVal(p):
    """
    StrVal : STRING
    """
    p[0] = p[1]

def p_Attribute(p):
    """
    Attribute : NAME
                | DESC
    """
    p[0] = p[1]

def p_Id(p):
    """
    Id : ID
    """
    p[0] = p[1]

def p_AddFunc(p):
    """
    AddFunc : ADD_OPTION
            | ADD_NEXT_SCENE
    """
    p[0] = p[1]

def p_DisplayFunc(p):
    """
    DisplayFunc : DISPLAY_SCENE
                | DISPLAY_OPTION
    """
    p[0] = p[1]

def p_Quit(p):
    """
    Quit : QUIT SEMICOLON
    """
    exit()

def p_Empty(p):
    'Empty :'
    p[0] = None


def p_error(p):
    print("Syntax Error: ", p)

parser = yacc.yacc()

### -------------------------------------------------------------------------------

# parser.parse(input = data, lexer = lexer)

# ----------------------------------------------

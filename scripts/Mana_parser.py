import sys
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
from .scene import Scene, Option
from .game_engine import GameEngine
# from scene import Scene, Option
# from game_engine import GameEngine

reference_log = {}
initialScene: Scene = None
debug: bool = False

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
    'CONCAT',
    'NEWLINE',
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
    'quit' : 'QUIT',
    'var' : 'VAR'
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
t_CONCAT = r'\+'
t_NEWLINE = r'\\n'

identifier = r'(' + t_CHARACTER + r'(' + t_CHARACTER + r'|' + t_DIGIT + r')*)'
string = r'(' + t_QUOM + r'([^\"])*' + t_QUOM + r')'

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

# data = """
# init shrine_entrance as Scene (
# 	name = "Shrine Entrance",
# 	desc = "A spooky shrine looms in front of you." + \\n + "A guard blocks your way."
# );
# """

# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

#---------------------------------------------------------

def p_Main(p):
    """
    Main : ExpList
    """
    p[0] = p[1]
    engine = GameEngine()
    if not debug:
        engine.loading_screen()
        engine.run_game(initialScene)

def p_Exp_Var(p):
    """
    Exp : VAR Id EQ StrVal SEMICOLON
    """
    p[0] = (p[1], p[2], p[4])
    reference_log[p[2]] = p[4]

def p_Exp_Init(p):
    """
    Exp : INIT Id AS ObjectDef
    """
    global initialScene
    p[0] = (p[1], p[2], p[4])
    try:
        reference_log[p[2]] = p[4]
    except:
        print("Referenced id already exists: ", p[2])
        return
    if isinstance(p[4], Scene) and initialScene == None:
        initialScene = p[4]

def p_Exp_AddFunc(p):
    """
    Exp : AddFunc Id TO Id SEMICOLON
    """
    p[0] = (p[1], p[2], p[4])
    try:
        child = reference_log[p[2]]
        paren = reference_log[p[4]]
    except KeyError:
        print("One or more referenced objects do not exist: ", p[0])
        return

    if p[1] == 'add_next_scene' and isinstance(child, Scene) and isinstance(paren, Scene):
        paren.add_next_scene(child)
    elif p[1] == 'add_option' and isinstance(child, Option) and isinstance(paren, Scene):
        paren.set_option(child)
    else:
        print("Referenced objects do not match function type: ", p[0])

def p_Exp_Display(p):
    """
    Exp : DisplayFunc Id SEMICOLON
    """
    p[0] = (p[1], p[2])
    try:
        obj = reference_log[p[2]]
    except KeyError:
        print("Referenced object does not exist: ", p[2])
        return
    if p[1] == 'display_scene' and isinstance(obj, Scene):
        obj.display_scene()
    elif p[1] == 'display_option' and isinstance(obj, Option):
        obj.display_option()
    else:
        print("Referenced object does not match function type: ", p[0])

def p_Exp_Modify(p):
    """
    Exp : MODIFY Id Def SEMICOLON
    """
    p[0] = (p[1], p[2], p[3])
    try:
        obj = reference_log[p[2]]
    except:
        print("Referenced object does not exist: ", p[2])
        return
    if isinstance(obj, Scene) :
        try:
            obj.modify_scene(p[3][0], p[3][1])
        except:
            print("Expected {} attributes unmatched".format(Scene))
            return
    elif isinstance(obj, Option) :
        try:
            obj.modify_option(p[3][0], p[3][1])
        except:
            print("Expected {} attributes unmatched".format(Option))
            return

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
        try:
            p[0] = Scene(p[2][0], p[2][1])
        except:
            print("Expected attributes for {} unmatched".format(Scene))
            return
    elif p[1] == 'Option':
        try:
            p[0] = Option(p[2][0], p[2][1])
        except:
            print("Expected attributes for {} unmatched".format(Option))
            return
    else:
        print("Unexpected object type: ", p[1])

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
                | Attribute EQ Id
    """
    try:
        val = reference_log[p[3]]
    except:
        val = p[3]
    p[1] = val
    p[0] = p[1]

def p_StrVal(p):
    """
    StrVal : StrList
    """
    p[0] = p[1]

def p_StrList(p):
    """
    StrList : STRING CONCAT StrList
            | STRING CONCAT NEWLINE CONCAT StrList
            | Id CONCAT NEWLINE CONCAT StrList
            | STRING
            | Id
    """
    try:
        strn = p[1].split('"')[1]
    except:
        strn = reference_log[p[1]]
    try:
        if not p[2]:
            p[0] = strn
        elif p[3] == "\\n":
            p[0] = strn + "\n" + p[5]
        else:
            p[0] = strn + p[3]
    except IndexError:
        p[0] = strn

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

# data = """
# init shrine_entrance as Scene (
# 	name = "Shrine Entrance",
# 	desc = "A spooky shrine looms in front of you." + \\n + "A guard blocks your way."
# );
# """

# parser.parse(input = data, lexer = lexer)

# ----------------------------------------------

from scripts import Mana_parser

parser = Mana_parser.parser
lexer = Mana_parser.lexer

file = open("testcode.txt", 'r')

s = ''
for line in file:
    s+=line

parser.parse(input = s, lexer = lexer)
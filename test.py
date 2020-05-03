from Mana_parser import parser, lexer

file = open("testcode.txt", 'r')

s = ''
for line in file:
    s+=line

parser.parse(input = s, lexer = lexer)
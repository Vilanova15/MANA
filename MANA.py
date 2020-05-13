import sys
from scripts import Mana_parser

inFile = sys.argv[1]
parser = Mana_parser.parser
lexer = Mana_parser.lexer

def main():
        
    file = open(inFile, 'r')

    s = ''
    for line in file:
        s+=line

    parser.parse(input = s, lexer = lexer)

if __name__ == '__main__':
    main()
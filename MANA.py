import sys
from Mana_parser import parser, lexer
import banner

inFile = sys.argv[1]

def main():
    banner.printbychar(("logo.txt", "banner.txt"))
        
    file = open(inFile, 'r')

    s = ''
    for line in file:
        s+=line

    parser.parse(input = s, lexer = lexer)

if __name__ == '__main__':
    main()
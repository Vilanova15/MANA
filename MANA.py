from Mana_parser import parser, lexer

def main():
    filename = input("File: ")
    file = open(filename, 'r')

    s = ''
    for line in file:
        s+=line

    parser.parse(input = s, lexer = lexer)

if __name__ == '__main__':
    main()
from Mana_parser import parser, lexer
import banner

def main():
    banner.printbychar(("logo.txt", "banner.txt"))

    try:
        filename = input("File: ")
    except:
        return
        
    file = open(filename, 'r')

    s = ''
    for line in file:
        s+=line

    parser.parse(input = s, lexer = lexer)

if __name__ == '__main__':
    main()
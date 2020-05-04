from Mana_parser import parser, lexer

def main():
    print("Welcome to MANA!\n")

    while True:
        try:
            s = input('>> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if not s: continue
        parser.parse(s, lexer=lexer)

if __name__ == '__main__':
    main()
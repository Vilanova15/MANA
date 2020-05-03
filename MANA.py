from Mana_parser import parser, lexer

def showBanner():
    banner = open("banner.txt", 'r')
    bannerStr = ''
    for line in banner:
        bannerStr += line
    print(bannerStr)

def main():
    showBanner()

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
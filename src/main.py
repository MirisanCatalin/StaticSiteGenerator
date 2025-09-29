#print('hello world')

from textnode import TextType, TextNode 

def main():
    ceva = TextNode('This is some anchor text', 'link', 'https://www.boot.dev')
    print(ceva)

if __name__ == '__main__':
    main()

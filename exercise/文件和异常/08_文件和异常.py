def main():
    f = open('demo.txt', 'r', encoding='utf-16')
    print(f.read(), end='')
    f.close()

if __name__ == '__main__':
    main()
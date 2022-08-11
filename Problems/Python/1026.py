
def main (a,b):
    print(4^6)
    print(a^b)


while True:

    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    main(a,b)

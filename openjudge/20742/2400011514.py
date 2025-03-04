def main():
    n = int(input())
    print(tnumber(n))

def tnumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tnumber(n - 1) + tnumber(n - 2) + tnumber(n - 3)


if __name__ == "__main__" :
    main()
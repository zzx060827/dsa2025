import sys
def oeSort(l):
    n = len(l)
    sortn = 0
    for i in range(sys.maxsize):
        sortn += 1
        for j in range(i%2, n-1, 2):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                sortn = 0
        print("{:3d}:{}".format(i, l))
        if sortn > 1:
            break

if __name__ == "__main__":
    n = int(input())
    oeSort( l:= list(reversed(range(n))))
    print(l)

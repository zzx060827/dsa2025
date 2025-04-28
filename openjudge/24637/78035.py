if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    l = [0] + l
    L = lambda i : l[i] if i<=n else 0
    for i in range(n, 0, -1):
        l[i] = max(L(2*i)+L(2*i+1), l[i]+L(4*i)+L(4*i+1)+L(4*i+2)+L(4*i+3))
    print(l[1])

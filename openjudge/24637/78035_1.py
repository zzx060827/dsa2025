if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    l = [0] + l
    def L(i):
        if i<=n:
            return max(L(2*i)+L(2*i+1), l[i]+L(4*i)+L(4*i+1)+L(4*i+2)+L(4*i+3))
        else:
            return 0
    print(L(1))

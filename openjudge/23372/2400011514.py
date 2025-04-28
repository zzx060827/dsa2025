import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        volumes = list(map(int, sys.stdin.readline().strip().split()))
        dp = [0] * (n + 1)
        dp[0] = 1
        for v in volumes:
            if v <= n:
                for j in range(v, n + 1):
                    dp[j] += dp[j - v]
        print(dp[n])

if __name__ == "__main__":
    main()
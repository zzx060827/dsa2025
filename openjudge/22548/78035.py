#
# 一维动规：问题规模加一，考虑最后一天卖出可能产生的
# 收益。在动规数组之外，还需要用数组记录前n天的最低价。
#
def max_gain(price):
    minp = [price[0]] * len(price)
    gain = [0] * len(price)
    for i in range(1, len(price)):
        minp[i] = min(minp[i-1], price[i])
        gain[i] = max(gain[i-1], price[i] - minp[i-1])
    return gain[-1]

if __name__ == "__main__":
    price = [int(x) for x in input().split()]
    if len(price) <= 0:
        raise ValueError("No input data")
    print(max_gain(price))

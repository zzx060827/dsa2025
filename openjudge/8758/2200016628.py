def convert(n):
    if n == 0:
        return "0"
    if n == 1:
        return "2(0)"
    if n == 2:
        return "2"
    
    res = []
    power = 0
    while n > 0:
        if n % 2 == 1:
            if power == 0:
                res.append("2(0)")
            elif power == 1:
                res.append("2")
            else:
                res.append(f"2({convert(power)})")
        n //= 2
        power += 1
    return '+'.join(reversed(res))

n = int(input())
print(convert(n))
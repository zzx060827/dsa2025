import hashlib

#挖矿对象
text = "区块：I am Santoshi Nakamoto"
#尝试不同的nonce（盐）值
for nonce in range(1000):
    input  = text + str(nonce)
    hash = hashlib.sha256(input.encode('utf8')).hexdigest()
    print("{} ==> {}".format(input, hash))
    difficult=2
    if (hash[:difficult]=='0'*difficult):
        print("恭喜您！获得比特币一枚。")
        break

import time

def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    return theSum

def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start

for i in range(5):
    print("Sum is %d required %10.7f seconds" 
       % sumOfN2(1000000))

def sumOfN3(n):
    start = time.time()
    theSum = (n * (n + 1 )) / 2
    end = time.time()
    return theSum, end - start

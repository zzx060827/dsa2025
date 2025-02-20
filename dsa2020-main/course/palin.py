from deque import Deque

def isPalindromic(str):
    dq = Deque()
    
    for c in str:
        dq.addFront(c)

    while dq.size()>1 :
        if dq.removeFront() != dq.removeRear():
            return False
    return True

if __name__ == "__main__":
    print("lsdkjfskf is {}".format(isPalindromic("lsdkjfskf")))
    print("radar is {}".format(isPalindromic("radar")))

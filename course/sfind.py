def sequentialSearch(alist, item):
    for elem in alist:
        if elem == item:
            return True
    return False

def orderedSequentialSearch(alist, item):
    for elem in alist:
        if elem == item:
            return True
        elif elem > item:
            return False
    return False

if __name__ == "__main__":
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

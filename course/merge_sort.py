def mergeSort(lst):
    if len(lst) <= 1:                         #基本结束条件
        return
    left, right = lst[:len(lst)//2], lst[len(lst)//2:]
    mergeSort(left)                           #递归调用
    mergeSort(right)
    lst.clear()
    i = j = 0
    while i < len(left) and j < len(right):   #拉链式归并剩余最小项
        if left[i] <= right[j] :
            lst.append(left[i])
            i += 1
        else :
            lst.append(right[j])
            j += 1
    else:                                     #归并所有剩余项
        lst.extend(left[i:] if i<len(left) else right[j:])
    return

if __name__ == "__main__":
    l = [1, 0, 0, 8, 6]
    mergeSort(l)
    print(l)

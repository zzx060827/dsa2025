def split(alist, first, last):
    """
    选第一个元素为中值，进行分裂
    """
    left, right = first+1, last-1     #左右标初值
    while left <= right:               #左右相错之前一直执行
        """ 访问元素之前先考虑下标是否越界 """
        while left<=right and alist[left] <= alist[first]:
            left += 1      #右移左标
        while right>=left and alist[right] >= alist[first]:
            right -= 1     #左移右标
        if left < right:   #交换左右标元素，并继续移动
            alist[left], alist[right] = alist[right], alist[left]
    else:                  #中值点就位
        alist[first], alist[right] = alist[right], alist[first]
    return right           #返回中值点位置

def quickSort(alist):
    _quickSort(alist, 0, len(alist))

def _quickSort(alist, first, last):  #递归形式函数
    if last - first > 1:  # more than 1 elems基本结束条件
        pivot = split(alist, first, last)  #分裂为左右两半
        _quickSort(alist, first, pivot)    #递归调用
        _quickSort(alist, pivot+1, last)

if __name__ == "__main__":
    quickSort(l:=[21,22,9]); print(l)
    quickSort(l:=[54,26,93,17,77,31,44,55,21]); print(l)

import sys
def merge_count(arr, temp_arr, left, mid, right):
    i = left  # 左子数组的起始索引
    j = mid + 1  # 右子数组的起始索引
    k = left  # 临时数组索引
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # 计算逆序对个数
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    return inv_count
def merge_sort_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_count(arr, temp_arr, left, mid, right)
    return inv_count
def count_inversions(arr, n):
    temp_arr = [0] * n
    return merge_sort_count(arr, temp_arr, 0, n - 1)
def main():
    input_data = sys.stdin.read().splitlines()
    index = 0
    while index < len(input_data):
        N = int(input_data[index])
        if N == 0:
            break
        arr = list(map(int, input_data[index + 1].split()))
        print(count_inversions(arr, N))
        index += 2
if __name__ == "__main__":
    main()

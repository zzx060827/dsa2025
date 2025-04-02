def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_merge = merge(left, right)
    total = inv_left + inv_right + inv_merge
    return merged, total

def merge(left, right):
    result = []
    i = j = 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions

if __name__ == "__main__":
    while True:
        N = int(input())
        if N == 0:
            break
        A = list(map(int, input().split()))
        _, ans = count_inversions(A)
        print(ans)

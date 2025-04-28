def mergeSort(nums,tmp,l,r):
    if l>=r:
        return 0

    mid = (l+r)//2
    count = mergeSort(nums,tmp,l,mid)+mergeSort(nums,tmp,mid+1,r)

    i,j,pos=l,mid+1,l
    while i <= mid and j <= r:
        if nums[i]<nums[j]:
            tmp[pos]=nums[i]
            count+= r-j+1
            i+=1
        else:
            tmp[pos]=nums[j]
            j+=1
        pos+=1

    for k in range(i,mid+1):
        tmp[pos] = nums[k]
        pos+=1

    for k in range(j,r+1):
        tmp[pos] = nums[k]
        pos+=1

    nums[l:r+1]=tmp[l:r+1]
    return count

def main():
    N = int(input())
    tmp=[0]*N
    nums = []
    for i in range(N):
        nums.append(int(input()))
    print(mergeSort(nums,tmp,0,N-1))

if __name__ =="__main__":
    main()
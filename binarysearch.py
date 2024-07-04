def binary_search(arr,target):
    left,right=0,len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif(arr[mid] < target):
            left=mid+1
        else:
            right=mid-1
            
    return -1
arr=[10,50,60,80,85]
result=binary_search(arr,80)
print(result)

###############################selection sort##########################3
def selection_sort(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
        arr[i],arr[min_val]=arr[min_val],arr[i]
    return arr
print(selection_sort([5,4,8,1,9,2]))
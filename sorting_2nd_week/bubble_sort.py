###############################3Bubble sort#######################################
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([5,8,1,3,2,0]))

######################optimized bubble sort####################################
def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped=False
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
print(bubble_sort([20,50,10,30,40]))
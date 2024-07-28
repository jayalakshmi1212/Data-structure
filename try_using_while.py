def bubble_sort(arr):
    i=0
    while(i<len(arr)-1):
        j=0
        while(j<len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        i+=1
    return arr
print(bubble_sort([4,2,5,1,3]))

def insertion_sort(arr):
    i=1
    while(i<len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        i+=1
    return arr
print(insertion_sort([4,2,5,1,3]))

def selection_sort(arr):
    i=0
    while(i<len(arr)):
        min_val=i
        j=i+1
        while(j<len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
            j+=1
        arr[i],arr[min_val]=arr[min_val],arr[i]   
        i+=1
    return arr
print(selection_sort([4,2,5,1,3]))

   
########################################## NADEEM'S CODE  ##################################################

def quickSort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)
        quickSort(array, left, partition_pos - 1)
        quickSort(array, partition_pos + 1, right)

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i

array = [2, 4, 16, 11, 21, 25, 32, 62, 41]
quickSort(array, 0, len(array) - 1)
print(array)

#########################################  MY CODE  #############################################################

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_elem = arr[0]
        less_than = [x for x in arr[1:] if x <= pivot_elem]
        grtr_than = [x for x in arr[1:] if x > pivot_elem]
        return quick_sort(less_than) + [pivot_elem] + quick_sort(grtr_than)

print(quick_sort([2, 5, 3, 1, 4]))



######################### javascript converted python code for quick sort   #################################

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)

arr = [4, 2, 5, 1, 3]
print(quicksort(arr))


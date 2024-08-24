def count_swap(arr):
    arr_sort = arr.copy()
    arr_sort.sort()
    temp = 0
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != arr_sort[i]:
            temp = arr_sort[i]
            arr[arr_sort.index(arr[i])] = arr[i]
            arr[i] = temp
            
            swaps += 1
    return(swaps)

print(count_swap([2, 5, 3, 1]))
print(count_swap([5, 2, 3, 1]))



